import requests
from bs4 import BeautifulSoup
headers = []
url='https://merolagani.com/StockQuote.aspx'
soup = BeautifulSoup(requests.get(url).text,"html.parser")
response = dict()
for i in soup.find_all("th"):
    headers.append(i.text.strip())
row_value = soup.find_all("tr")
for i in row_value:
    dict1 = dict()
    try:
        name = i.find("a",{"tabindex":"-1"}).get("title").strip()
        dict1.update({'Name':name})
    except:
        pass
    data = i.find_all("td")
    for n,j in enumerate(data):
        if headers[n].strip() != "#":
            key = headers[n]
            value = data[n].text.strip()
            dict1.update({key:value})
    try:
        symbol = dict1.get('Symbol')
        dict1.pop('Symbol')
        response.update({symbol:dict1})
    except:
        pass
print(response)
