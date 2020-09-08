import requests
from bs4 import BeautifulSoup
import json

def todaysPrice(url):

    header_list = []
    response = dict()

    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    head_value = soup.find_all("th")
    row_value = soup.find_all("tr")
    
    for i in head_value:
        head = i.text.strip().lower()
        if head == 'conf.' :
            head = 'conf'
        elif head == 'trans.':
            head = 'transfer'
        elif head == 'diff %':
            head = 'diff_per'
        elif head == 'range %':
            head = 'range_per'
        elif head == 'vwap %':
            head = 'vwap_per'      
        header_list.append(head)
  
    for i in row_value:
        dict1 = dict()
        data = i.find_all("td")
        for n,j in enumerate(data):
            if header_list[n].strip() != "s.no":
                key = header_list[n]
                value = j.text.strip()
                dict1.update({key:value})
            if header_list[n].strip()=="symbol":
                name=j.find('a').get('title')
                dict1.update({'name':name})

        try:
            symbol = dict1.get('symbol')
            dict1.pop('symbol')
            response.update({symbol:dict1})
        except:
            pass
        
    json_response = json.dumps(response,indent=4)
    return json_response
