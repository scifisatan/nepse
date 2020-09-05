
import requests
from bs4 import BeautifulSoup
import json
from flask import Flask

headers = []
response = dict()
app = Flask(__name__)
url='https://www.sharesansar.com/today-share-price'

def api(url):
    soup = BeautifulSoup(requests.get(url).text,"html.parser")
    for i in soup.find_all("th"):
        headers.append(i.text.strip())
    row_value = soup.find_all("tr")
    for i in row_value:
        dict1 = dict()

        data = i.find_all("td")
        for n,j in enumerate(data):
            if headers[n].strip() != "S.No":
                key = headers[n]
                value = data[n].text.strip()
                dict1.update({key:value})
            if headers[n].strip()=="Symbol":
                name=data[n].find('a').get('title')
                dict1.update({'Name':name})

        try:
            symbol = dict1.get('Symbol')
            dict1.pop('Symbol')
            response.update({symbol:dict1})
        except:
            pass

    json_response = json.dumps(response,indent=4)
    return json_response

@app.route("/")
@app.route("/home")
def home():
    return api(url)

if __name__ == '__main__':
    app.run(debug=True)
