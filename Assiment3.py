import requests
from bs4 import BeautifulSoup
import csv
import json


tag_types =  ["p", "strong"]

def get_all_nodes_by_tag_types(node, tag_types):
  """
  Extracts all nodes from specific tag types within the provided HTML string.

  Args:
      html_content: A string containing the HTML content.
      tag_types: A list of strings representing the desired tag types (e.g., ["p", "strong", "li", "u"]).

  Returns:
      A list of BeautifulSoup element objects representing the found nodes.
  """
  # Parse the HTML content
#   soup = BeautifulSoup(html_content, 'html.parser')

  # Find all nodes matching the specified tag types
  all_nodes = []
  for tag_type in tag_types:
    nodes = node.find_all(tag_type)
    all_nodes.extend(nodes)  # Extend the list with nodes of each type

  return all_nodes

def extract_all_text(elements):
  text = ''
  for child in elements:
        if child.text is not None:
         text += child.text  # Recursively extract from children
  return text


def loadDeseaseDetail(url):

    cookies = {
        'VISITOR-ID': 'a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451',
        'abVisitorId': '477912',
        'abExperimentShow': 'true',
        '_csrf': 'CIyFNZGaCT7wNB7QnzfMmVwk',
        'jarvis-id': '62fad9f5-1c5d-4139-8815-66b3513f5a4e',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2BOsBJfj4KyQQgIUT12Jb9bqaEYwRIRDTg%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19PxdJPA%2FnhAyjZIRENCh47e9I26fysN4U%3D',
        'geolocation': 'false',
        'synapse:init': 'false',
        'synapse:platform': 'web',
        'session': 'SevpeJFuYqmzS_Fz7Oj0KQ.IR9qY0s5al0he8-E14cYCdoa2t9AkqXMWQRG3-QkvifzMvFcIgbFzqKngM3GfeFv-SLjVis4YH7q06Qv1SadZ-C9wULC2CtevJVcTlBugU26KpNxm4u86fRCs3vpxyu9KYbhY1ZzKYW0pz6NQP0bqQ.1718352528383.144000000.fXD6_sxkWs_wkr_3W50fwWpPOtQZdOmU1euWAJgyUhM',
        '_fbp': 'fb.1.1718352529159.501471814294124913',
        '_gcl_au': '1.1.600772368.1718352529',
        '_gid': 'GA1.2.1293079735.1718352529',
        'singular_device_id': '8f3cd9cf-bdad-4995-80ab-fc392be80fa8',
        '_nv_did': '173339004.1718352529.11614185239yvtkv',
        '__adroll_fpc': '1da2e5145707ac4c3a0fe91fd226e95a-1718352529538',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%2227qi3r4Ko0G4kMdCVl0I%22%7D',
        'shw_13453': '1',
        'locale': 'en',
        'city': 'Aurangabad Maharashtra',
        'latitude': '1.3123516',
        'longitude': '103.9375239',
        'pincode': '',
        'polygonIDs': '',
        'addressText': 'Aurangabad Maharashtra',
        'addressSubtext': '',
        'addressType': '',
        'demandClusterId': '',
        'TMP_HKP_USER_ID': 'a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451',
        'amoSessionId': '6cccc36a-262a-4a19-ac7f-21f3901f7c6b',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_nv_sess': '173339004.1718372012.Oie3SzwJUBNdQyt0nue68F1TykWQjnkXsk2Yk548auyhp289Vi',
        '_nv_uid': '173339004.1718352529.2ddbd110-7c7b-4528-a80e-bf4615a09183.1718352529.1718372012.2.0',
        '_nv_utm': '173339004.1718352529.2.1.dXRtc3JjPShkaXJlY3QpfHV0bWNjbj0oZGlyZWN0KXx1dG1jbWQ9KG5vbmUpfHV0bWN0cj0obm90IHNldCl8dXRtY2N0PShub3Qgc2V0KXxnY2xpZD0obm90IHNldCk=',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FX4Wb%2F5XKIgMJCPDb%2FUM0%2BTZPdHfQmesc%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2FwwXoU0yxMfFUUHk1gZac10a7E0rzemK0%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX18qsIjlQgJXRiulwyG%2F7ZBnZFGQ8W%2BX2Wk%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX18Vho9ALlfUphvTa4WzmhoxgSuP1ZokMR4%3D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX19lu2Q4FL%2BiSRrOzGH4lpOXp5mCsFFxEZXBDH6%2Bl2SsrAmcYeKKQZbZD47DiFCuMBZh%2F9cbwDPeug%3D%3D',
        'rl_session': 'RudderEncrypt%3AU2FsdGVkX19uVdv0F%2BE%2BI4s%2BC%2FAWwiNO7vJFTh8lPhqhpb6Il1hgHANACagc8l2LhTCAJypNNN2A2BRGGeS9%2F4AWZvxe3jJ3csTI8JbxqWao4iwls25Sd71VvjroeCodxXlD2EV8DdeZLdf3RzgQxA%3D%3D',
        '_uetsid': '5480c0702a2511ef86dd21339498edd5',
        '_uetvid': '5480aeb02a2511efafc1e5aedd817c80',
        '_ga_1HF6RR2VT7': 'GS1.1.1718372012.2.1.1718372055.0.0.0',
        '_ga': 'GA1.1.136591370.1718352529',
        '__ar_v4': 'KJTLL7NSNRFA5J3GVYGJVJ%3A20240614%3A6%7C6PFMKMAZXFGFLMSXPCJHFF%3A20240614%3A6%7CU4ZFS2QH4VB65A54O43AEQ%3A20240614%3A6',
        '_nv_hit': '173339004.1718372055.cHZpZXc9Mg==',
        'fs_uid': '#11EGJ5#6515379731247104:3439498338768641830:::#/1749888535',
        '_ga_NPGHGVF7FB': 'GS1.1.1718372012.2.1.1718372068.4.0.0',
        'AWSALBTG': 'bm+/Seji1N61I6/p0uDXEx5sVFY1e2rSzpVWBVPnMp2RcKuIiofesKd1QElY3buWkcUy+Fe+vrCRyoYg1Nrn76kuiWT+lEp6urftsvG1XGRXnQAZDoywR8RXzx7P1wdgxtJ1XVvqOOQW0I2kzTTzr+diuBroBqtjW2xlSjQRW6wV',
        'AWSALBTGCORS': 'bm+/Seji1N61I6/p0uDXEx5sVFY1e2rSzpVWBVPnMp2RcKuIiofesKd1QElY3buWkcUy+Fe+vrCRyoYg1Nrn76kuiWT+lEp6urftsvG1XGRXnQAZDoywR8RXzx7P1wdgxtJ1XVvqOOQW0I2kzTTzr+diuBroBqtjW2xlSjQRW6wV',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'VISITOR-ID=a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451; abVisitorId=477912; abExperimentShow=true; _csrf=CIyFNZGaCT7wNB7QnzfMmVwk; jarvis-id=62fad9f5-1c5d-4139-8815-66b3513f5a4e; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BOsBJfj4KyQQgIUT12Jb9bqaEYwRIRDTg%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19PxdJPA%2FnhAyjZIRENCh47e9I26fysN4U%3D; geolocation=false; synapse:init=false; synapse:platform=web; session=SevpeJFuYqmzS_Fz7Oj0KQ.IR9qY0s5al0he8-E14cYCdoa2t9AkqXMWQRG3-QkvifzMvFcIgbFzqKngM3GfeFv-SLjVis4YH7q06Qv1SadZ-C9wULC2CtevJVcTlBugU26KpNxm4u86fRCs3vpxyu9KYbhY1ZzKYW0pz6NQP0bqQ.1718352528383.144000000.fXD6_sxkWs_wkr_3W50fwWpPOtQZdOmU1euWAJgyUhM; _fbp=fb.1.1718352529159.501471814294124913; _gcl_au=1.1.600772368.1718352529; _gid=GA1.2.1293079735.1718352529; singular_device_id=8f3cd9cf-bdad-4995-80ab-fc392be80fa8; _nv_did=173339004.1718352529.11614185239yvtkv; __adroll_fpc=1da2e5145707ac4c3a0fe91fd226e95a-1718352529538; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%2227qi3r4Ko0G4kMdCVl0I%22%7D; shw_13453=1; locale=en; city=Aurangabad Maharashtra; latitude=1.3123516; longitude=103.9375239; pincode=; polygonIDs=; addressText=Aurangabad Maharashtra; addressSubtext=; addressType=; demandClusterId=; TMP_HKP_USER_ID=a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451; amoSessionId=6cccc36a-262a-4a19-ac7f-21f3901f7c6b; AMP_TOKEN=%24NOT_FOUND; _nv_sess=173339004.1718372012.Oie3SzwJUBNdQyt0nue68F1TykWQjnkXsk2Yk548auyhp289Vi; _nv_uid=173339004.1718352529.2ddbd110-7c7b-4528-a80e-bf4615a09183.1718352529.1718372012.2.0; _nv_utm=173339004.1718352529.2.1.dXRtc3JjPShkaXJlY3QpfHV0bWNjbj0oZGlyZWN0KXx1dG1jbWQ9KG5vbmUpfHV0bWN0cj0obm90IHNldCl8dXRtY2N0PShub3Qgc2V0KXxnY2xpZD0obm90IHNldCk=; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FX4Wb%2F5XKIgMJCPDb%2FUM0%2BTZPdHfQmesc%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2FwwXoU0yxMfFUUHk1gZac10a7E0rzemK0%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18qsIjlQgJXRiulwyG%2F7ZBnZFGQ8W%2BX2Wk%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX18Vho9ALlfUphvTa4WzmhoxgSuP1ZokMR4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19lu2Q4FL%2BiSRrOzGH4lpOXp5mCsFFxEZXBDH6%2Bl2SsrAmcYeKKQZbZD47DiFCuMBZh%2F9cbwDPeug%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX19uVdv0F%2BE%2BI4s%2BC%2FAWwiNO7vJFTh8lPhqhpb6Il1hgHANACagc8l2LhTCAJypNNN2A2BRGGeS9%2F4AWZvxe3jJ3csTI8JbxqWao4iwls25Sd71VvjroeCodxXlD2EV8DdeZLdf3RzgQxA%3D%3D; _uetsid=5480c0702a2511ef86dd21339498edd5; _uetvid=5480aeb02a2511efafc1e5aedd817c80; _ga_1HF6RR2VT7=GS1.1.1718372012.2.1.1718372055.0.0.0; _ga=GA1.1.136591370.1718352529; __ar_v4=KJTLL7NSNRFA5J3GVYGJVJ%3A20240614%3A6%7C6PFMKMAZXFGFLMSXPCJHFF%3A20240614%3A6%7CU4ZFS2QH4VB65A54O43AEQ%3A20240614%3A6; _nv_hit=173339004.1718372055.cHZpZXc9Mg==; fs_uid=#11EGJ5#6515379731247104:3439498338768641830:::#/1749888535; _ga_NPGHGVF7FB=GS1.1.1718372012.2.1.1718372068.4.0.0; AWSALBTG=bm+/Seji1N61I6/p0uDXEx5sVFY1e2rSzpVWBVPnMp2RcKuIiofesKd1QElY3buWkcUy+Fe+vrCRyoYg1Nrn76kuiWT+lEp6urftsvG1XGRXnQAZDoywR8RXzx7P1wdgxtJ1XVvqOOQW0I2kzTTzr+diuBroBqtjW2xlSjQRW6wV; AWSALBTGCORS=bm+/Seji1N61I6/p0uDXEx5sVFY1e2rSzpVWBVPnMp2RcKuIiofesKd1QElY3buWkcUy+Fe+vrCRyoYg1Nrn76kuiWT+lEp6urftsvG1XGRXnQAZDoywR8RXzx7P1wdgxtJ1XVvqOOQW0I2kzTTzr+diuBroBqtjW2xlSjQRW6wV',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'service-worker-navigation-preload': 'true',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
    }

    response = requests.get(url=url, cookies=cookies, headers=headers)
    i = 1
    finalObj = {}
    # field names are not mapped correctly now.
    keyNames = ['keyfacts', 'symptoms', 'causes', 'types', 'risk_factors', 'daignosis', 'prevention', 'special_visit', 'treatment', 'home_care', 'alternative_therapy', 'living_with', 'faqs', 'references']
    startString = "window._INITIAL_STATE_ = "
    endString = ";\n                    window._STATUS_CODE_ = null;"
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.findAll("script")
        for script in scripts:
           if script.text is not None and script.text.strip().startswith(startString):
              probableJson = get_substring(script.text, startString, endString)
              jsonObj = json.loads(probableJson)
              widgets = jsonObj["diseasePageReducer"]["data"]["result"]["dynamicWidgets"]
              counter = 0
              for widget in widgets:
                 if counter >= len(keyNames):
                    break
                 if "content" in widget:
                    finalObj[keyNames[counter]] = BeautifulSoup(widget["content"], "html.parser").get_text()
                 else:
                    if "warnings" in widget:
                        keyFacts = ""
                        for keyfact in widget["warnings"]:
                           keyFacts = keyFacts + keyfact["imageCaption"]+ ": " + BeautifulSoup(keyfact["description"], "html.parser").get_text(strip=True) + "\n"
                        finalObj[keyNames[counter]] = keyFacts
                 counter = counter + 1
              break
        return finalObj
    else:
        print("Unable to download the detail")
        return {}

def get_substring(string, string1, string2):
  """
  Extracts the substring between string1 (inclusive) and string2 (exclusive).

  Args:
      string: The input string.
      string1: The starting string (inclusive).
      string2: The ending string (exclusive).

  Returns:
      The extracted substring, or None if not found.
  """
  start_index = string.find(string1)
  if start_index != -1:
    end_index = string.find(string2)
    if end_index != -1 and end_index > start_index:
      # Extract substring starting after string1 (inclusive) and ending before string2 (exclusive)
      return string[start_index + len(string1):end_index]
  return None

# Example usage
test_string = "This is a test string1with some contentstring2 and more text"
substring = get_substring(test_string, "string1", "string2")

if substring:
  print("Extracted substring:", substring)
else:
  print("Substring not found")

# loadDeseaseDetail('https://www.1mg.com/diseases/baby-colic-982')


def loadDeseasList(char):
    cookies = {
        'VISITOR-ID': 'a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451',
        'abVisitorId': '477912',
        'abExperimentShow': 'true',
        '_csrf': 'CIyFNZGaCT7wNB7QnzfMmVwk',
        'jarvis-id': '62fad9f5-1c5d-4139-8815-66b3513f5a4e',
        'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2BOsBJfj4KyQQgIUT12Jb9bqaEYwRIRDTg%3D',
        'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX19PxdJPA%2FnhAyjZIRENCh47e9I26fysN4U%3D',
        'geolocation': 'false',
        'synapse:init': 'false',
        'synapse:platform': 'web',
        'session': 'SevpeJFuYqmzS_Fz7Oj0KQ.IR9qY0s5al0he8-E14cYCdoa2t9AkqXMWQRG3-QkvifzMvFcIgbFzqKngM3GfeFv-SLjVis4YH7q06Qv1SadZ-C9wULC2CtevJVcTlBugU26KpNxm4u86fRCs3vpxyu9KYbhY1ZzKYW0pz6NQP0bqQ.1718352528383.144000000.fXD6_sxkWs_wkr_3W50fwWpPOtQZdOmU1euWAJgyUhM',
        '_fbp': 'fb.1.1718352529159.501471814294124913',
        '_gcl_au': '1.1.600772368.1718352529',
        '_gid': 'GA1.2.1293079735.1718352529',
        'singular_device_id': '8f3cd9cf-bdad-4995-80ab-fc392be80fa8',
        '_nv_did': '173339004.1718352529.11614185239yvtkv',
        '__adroll_fpc': '1da2e5145707ac4c3a0fe91fd226e95a-1718352529538',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%2227qi3r4Ko0G4kMdCVl0I%22%7D',
        'shw_13453': '1',
        'locale': 'en',
        'city': 'Aurangabad Maharashtra',
        'latitude': '1.3123516',
        'longitude': '103.9375239',
        'pincode': '',
        'polygonIDs': '',
        'addressText': 'Aurangabad Maharashtra',
        'addressSubtext': '',
        'addressType': '',
        'demandClusterId': '',
        'TMP_HKP_USER_ID': 'a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451',
        '_nv_uid': '173339004.1718352529.2ddbd110-7c7b-4528-a80e-bf4615a09183.1718352529.1718372012.2.0',
        '_nv_utm': '173339004.1718352529.2.1.dXRtc3JjPShkaXJlY3QpfHV0bWNjbj0oZGlyZWN0KXx1dG1jbWQ9KG5vbmUpfHV0bWN0cj0obm90IHNldCl8dXRtY2N0PShub3Qgc2V0KXxnY2xpZD0obm90IHNldCk=',
        '_uetsid': '5480c0702a2511ef86dd21339498edd5',
        '_uetvid': '5480aeb02a2511efafc1e5aedd817c80',
        '_nv_hit': '173339004.1718372055.cHZpZXc9Mg==',
        'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2F37aYDXUweiDyCNqTKAk0NrW6ZhEeiSJw%3D',
        'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2F8tjKl7XRH5kT3iZPsWd1hUlSqmjMlPKQ%3D',
        'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX1%2BDsH3naYXz7cNWvxK9eJYoajKfA6o%2BnR8%3D',
        'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19XCxFDjWy9cGHTn%2BvJRhrDZKoWbSpE9J8%3D',
        'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2Bsr6l8C5VNeg%2FCIbsAKgmsm%2BYo77w0qBYdGrv0HPXfdAdc1nRAQ21clbRmlj6F7LdsjNgz9g7B0A%3D%3D',
        '_ga_1HF6RR2VT7': 'GS1.1.1718375138.3.1.1718375676.0.0.0',
        '_ga': 'GA1.2.136591370.1718352529',
        '__ar_v4': 'KJTLL7NSNRFA5J3GVYGJVJ%3A20240614%3A10%7C6PFMKMAZXFGFLMSXPCJHFF%3A20240614%3A10%7CU4ZFS2QH4VB65A54O43AEQ%3A20240614%3A10',
        'fs_uid': '#11EGJ5#6515379731247104:3237491351170738873:::#/1749888542',
        'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2FWJ3DFZ6rWwCYHKbW2KRYcDDdDE0IgpAlzuC5KkKnEWw9Eslk5EplNFkbtDA83wJop8hBeimo%2Fspxfhlqa29lXsapahx2X95SWMGZFownJm2%2F8G4Q9hhqAR8IsoQ7NKz6oLMrq2W2rZA%3D%3D',
        'AWSALBTG': 'WNKmA1Tv4Dm/gKjJrPfsK8gX6OSM9rhmAwn0qNi+YJjatL2Xgliv4D0LNBdko1KKWFeH1WnKDm7j9BFArdVMaCc6ckF8Z1Q+NxgwNdOk9Z2lYpVjVQJd2fJnD9YpsSwhLsMvt6zG9E7I48Cu+LAgFAttZYBXcQwyRkHzyHTyo2xM',
        'AWSALBTGCORS': 'WNKmA1Tv4Dm/gKjJrPfsK8gX6OSM9rhmAwn0qNi+YJjatL2Xgliv4D0LNBdko1KKWFeH1WnKDm7j9BFArdVMaCc6ckF8Z1Q+NxgwNdOk9Z2lYpVjVQJd2fJnD9YpsSwhLsMvt6zG9E7I48Cu+LAgFAttZYBXcQwyRkHzyHTyo2xM',
        '_ga_NPGHGVF7FB': 'GS1.1.1718378479.4.1.1718380185.60.0.0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        # 'cookie': 'VISITOR-ID=a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451; abVisitorId=477912; abExperimentShow=true; _csrf=CIyFNZGaCT7wNB7QnzfMmVwk; jarvis-id=62fad9f5-1c5d-4139-8815-66b3513f5a4e; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BOsBJfj4KyQQgIUT12Jb9bqaEYwRIRDTg%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19PxdJPA%2FnhAyjZIRENCh47e9I26fysN4U%3D; geolocation=false; synapse:init=false; synapse:platform=web; session=SevpeJFuYqmzS_Fz7Oj0KQ.IR9qY0s5al0he8-E14cYCdoa2t9AkqXMWQRG3-QkvifzMvFcIgbFzqKngM3GfeFv-SLjVis4YH7q06Qv1SadZ-C9wULC2CtevJVcTlBugU26KpNxm4u86fRCs3vpxyu9KYbhY1ZzKYW0pz6NQP0bqQ.1718352528383.144000000.fXD6_sxkWs_wkr_3W50fwWpPOtQZdOmU1euWAJgyUhM; _fbp=fb.1.1718352529159.501471814294124913; _gcl_au=1.1.600772368.1718352529; _gid=GA1.2.1293079735.1718352529; singular_device_id=8f3cd9cf-bdad-4995-80ab-fc392be80fa8; _nv_did=173339004.1718352529.11614185239yvtkv; __adroll_fpc=1da2e5145707ac4c3a0fe91fd226e95a-1718352529538; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%2227qi3r4Ko0G4kMdCVl0I%22%7D; shw_13453=1; locale=en; city=Aurangabad Maharashtra; latitude=1.3123516; longitude=103.9375239; pincode=; polygonIDs=; addressText=Aurangabad Maharashtra; addressSubtext=; addressType=; demandClusterId=; TMP_HKP_USER_ID=a265f4f1-dc8b-48d5-bd27-d36495a66d8f_axu3RpCh38_0382_1718352526451; _nv_uid=173339004.1718352529.2ddbd110-7c7b-4528-a80e-bf4615a09183.1718352529.1718372012.2.0; _nv_utm=173339004.1718352529.2.1.dXRtc3JjPShkaXJlY3QpfHV0bWNjbj0oZGlyZWN0KXx1dG1jbWQ9KG5vbmUpfHV0bWN0cj0obm90IHNldCl8dXRtY2N0PShub3Qgc2V0KXxnY2xpZD0obm90IHNldCk=; _uetsid=5480c0702a2511ef86dd21339498edd5; _uetvid=5480aeb02a2511efafc1e5aedd817c80; _nv_hit=173339004.1718372055.cHZpZXc9Mg==; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2F37aYDXUweiDyCNqTKAk0NrW6ZhEeiSJw%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2F8tjKl7XRH5kT3iZPsWd1hUlSqmjMlPKQ%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BDsH3naYXz7cNWvxK9eJYoajKfA6o%2BnR8%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19XCxFDjWy9cGHTn%2BvJRhrDZKoWbSpE9J8%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2Bsr6l8C5VNeg%2FCIbsAKgmsm%2BYo77w0qBYdGrv0HPXfdAdc1nRAQ21clbRmlj6F7LdsjNgz9g7B0A%3D%3D; _ga_1HF6RR2VT7=GS1.1.1718375138.3.1.1718375676.0.0.0; _ga=GA1.2.136591370.1718352529; __ar_v4=KJTLL7NSNRFA5J3GVYGJVJ%3A20240614%3A10%7C6PFMKMAZXFGFLMSXPCJHFF%3A20240614%3A10%7CU4ZFS2QH4VB65A54O43AEQ%3A20240614%3A10; fs_uid=#11EGJ5#6515379731247104:3237491351170738873:::#/1749888542; rl_session=RudderEncrypt%3AU2FsdGVkX1%2FWJ3DFZ6rWwCYHKbW2KRYcDDdDE0IgpAlzuC5KkKnEWw9Eslk5EplNFkbtDA83wJop8hBeimo%2Fspxfhlqa29lXsapahx2X95SWMGZFownJm2%2F8G4Q9hhqAR8IsoQ7NKz6oLMrq2W2rZA%3D%3D; AWSALBTG=WNKmA1Tv4Dm/gKjJrPfsK8gX6OSM9rhmAwn0qNi+YJjatL2Xgliv4D0LNBdko1KKWFeH1WnKDm7j9BFArdVMaCc6ckF8Z1Q+NxgwNdOk9Z2lYpVjVQJd2fJnD9YpsSwhLsMvt6zG9E7I48Cu+LAgFAttZYBXcQwyRkHzyHTyo2xM; AWSALBTGCORS=WNKmA1Tv4Dm/gKjJrPfsK8gX6OSM9rhmAwn0qNi+YJjatL2Xgliv4D0LNBdko1KKWFeH1WnKDm7j9BFArdVMaCc6ckF8Z1Q+NxgwNdOk9Z2lYpVjVQJd2fJnD9YpsSwhLsMvt6zG9E7I48Cu+LAgFAttZYBXcQwyRkHzyHTyo2xM; _ga_NPGHGVF7FB=GS1.1.1718378479.4.1.1718380185.60.0.0',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'service-worker-navigation-preload': 'true',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'label': char,
    }
    response = requests.get('https://www.1mg.com/all-diseases', params=params, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    deseases = soup.findAll('a', attrs={'class': 'Card_productCardSrdLF marginTop-4 Cardtext_jeyhg'})
    results = []
    for desease in deseases:
       href = "https://www.1mg.com" + desease.get('href')
       titleDiv = desease.find('p', attrs= {'class': 'Card_productName_qw2CE bodyMedium'})
       results.append({'name': titleDiv.text, 'url': href})
    return results
       
def writeJsonToCSV(jsonArray, fileName):
    fieldnames = jsonArray[0].keys()
    with open("data.csv", "w", newline="") as csvfile:
    # Create a CSV writer object
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write the header row with field names
        csv_writer.writeheader()

        # Write each dictionary as a row in the CSV, handling missing keys
        for item in jsonArray:
            # Use get method to handle missing keys and provide an empty string as default
            row = {key: item.get(key, "") for key in fieldnames}
            csv_writer.writerow(row)


# Test case to be executed
# Constant variable by convention (uppercase)
inputAlphabets =  [chr(i) for i in range(ord('a'), ord('z') + 1)]
deseasList = []
for ch in inputAlphabets:
   print('List desease names for letters starting with ', ch)
   print('........')
   deseasList = deseasList + loadDeseasList(ch)
for des in deseasList:
   print('Loading desease detail for desease ', des["name"], "from url ", des["url"])
   print('........')
   detail = loadDeseaseDetail(des["url"])
   des.update(detail)
print("now printing the result into csv file ....")
writeJsonToCSV(deseasList, "data.csv")
print("Process completed successfully.")