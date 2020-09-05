import requests
import lxml.html as lh


url='http://www.nepalstock.com/main/todays_price'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML

tr_elements = doc.xpath('//*[@id="home-contents"]/table')
#Create empty list
data=""
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    data= data+name

print(data)