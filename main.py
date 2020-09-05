import requests
import lxml.html as lh


url='https://merolagani.com/StockQuote.aspx'
page = requests.get(url)
doc = lh.fromstring(page.content)

elements = doc.xpath('//*[@id="ctl00_ContentPlaceHolder1_divData"]/div[3]/table')

data=""
i=0

for t in elements:
    i+=1
    name=t.text_content()
    data= data+name

print(data)