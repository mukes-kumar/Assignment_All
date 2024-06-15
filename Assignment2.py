import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlparse, parse_qs

urls = []
def crawl_linkRecursively(requrl, level, maxLevel):
    if level == maxLevel:
        return
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url=requrl, headers=headers)
    # print(response.content)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extracting URLs from search results
        for link in soup.find_all('a', {'class': 'result__url'}):
            href = link.get('href')
            title = link.text
            if title is None:
                title = "N/A"
            if href:
                urls.append({title, href})
                crawl_linkRecursively(href, level=level+1, maxLevel=maxLevel)
        return urls
    else:
        print("Failed to fetch search results.")
        return []
    

def fetch_urls(primary_category, secondary_category, geography, date_range):
    # Constructing the search query based on input parameters
    search_query = f"{primary_category} {secondary_category} {geography} {date_range}"

    # Using DuckDuckGo search engine to search for URLs based on the search query
    # //search_url = f"https://duckduckgo.com/html/?q={search_query}"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'q': search_query,
    }

    response = requests.get('https://html.duckduckgo.com/html/', params=params, headers=headers)
    # print()
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    # }
    # crawl_linkRecursively(search_url, 0, 2)
    # response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extracting URLs from search results
        urls = []
        for link in soup.find_all('h2', {'class': 'result__title'}):
            linkItem = link.find('a')
            href = linkItem.get('href')
            title = linkItem.text
            # break
            finalUrl = "http:" + href
            parsed_url = urlparse(finalUrl)
            # Extract the query string
            query_string = parsed_url.query
            # Loop over key-value pairs (assuming a single parameter)
            parameter_value = ""
            for key, value in parse_qs(query_string).items():
            # Extract the actual value (assuming a single value per key)
                parameter_value = value[0]
            #    // print(parameter_value)
                urls.append({title, parameter_value})
                crawl_linkRecursively(parameter_value, 0, 2)
                break  # Assuming you only need the first parameter            
        return urls
    else:
        print("Failed to fetch search results.")
        return []

def save_to_csv(urls, output_file):
    # Writing URLs to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for url in urls:
            writer.writerow({'URL': url})

def web_crawler(input_params, output_file):
    primary_category = input_params.get('Primary Category', '')
    secondary_category = input_params.get('Secondary Category', '')
    geography = input_params.get('Geography', '')
    date_range = input_params.get('Date Range', '')

    urls = fetch_urls(primary_category, secondary_category, geography, date_range)
    if urls:
        save_to_csv(urls, output_file)
        print("URLs saved to", output_file)
    else:
        print("No URLs found.")

# Example input parameters
input_params = {
    "Primary Category": "Medical Journal",
    "Secondary Category": "Orthopedic",
    "Geography": "US",
    "Date Range": "2022"
}

output_file = "urls.csv"
web_crawler(input_params,output_file)