import requests
from bs4 import BeautifulSoup
import json

def floorSheet(url):

   
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")

    response = dict()
    header = soup.find_all("tr")[1]
    head_value = header.find_all('td')
    header_list = list()
    row_value = list()
    rows = soup.find_all('tr')

    for i in head_value:
        head = i.text.strip().lower()
        header_list.append(head)

    j = 1
    while j != len(rows):
        try:
            j += 1
            row_value.append(rows[j])
        except:
            pass
        
    for i in row_value:
        dict1 = dict()
        data = i.find_all("td")
        for n,j in enumerate(data):
            if header_list[n].strip() != "s.n.":
                key = header_list[n]
                value = data[n].text.strip()
                dict1.update({key:value})
        try:
            contract = dict1.get('contract no')
            dict1.pop('contract no')
            response.update({contract:dict1})
        except:
            pass
        
    json_response = json.dumps(response,indent=4)
    return json_response