import requests
import lxml.html as lh


url='http://www.nepalstock.com/main/todays_price'
page = requests.get(url)
doc = lh.fromstring(page.content)

elements = doc.xpath('//*[@id="home-contents"]/table')

data=""
i=0

for t in elements[0]:
    i+=1
    name=t.text_content()
    data= data+name

print(data)