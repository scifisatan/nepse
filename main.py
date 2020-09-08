import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, render_template
from todays_price import todaysPrice
from floor_sheet import floorSheet

app = Flask(__name__)
url1 = 'https://www.sharesansar.com/today-share-price'
url2 = 'http://www.nepalstock.com/main/floorsheet/index/1/?contract-no=&stock-symbol=&buyer=&seller=&_limit=10000'



@app.route("/")
@app.route("/home")
def home():
    return render_template('homepg.html')

@app.route("/floor_sheet")
def fs():
    return floorSheet(url2)

@app.route("/todays_price")
def tp():
    return todaysPrice(url1)
    
if __name__ == '__main__':
    app.run()
