from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
#1. create connection
url = "https://dantri.com.vn"
conn = urlopen(url)

#2. download page
raw_data = conn.read()
page_content = raw_data.decode("utf8")
    #print (page_content)

with open("dantri.html", "wb") as f:
    f.write(raw_data)

#3. find ROI
soup = BeautifulSoup(page_content, "html.parser")
ul=soup.find("div", "ul1 ulnew")
    #print(ul.prettify())

#4. extract ROI (phan giai)
li_list = ul.find_all('li')
#li = li_list[0]

new_list=[]
for li in li_list:
    h4=li.h4
    a=h4.a
    link =url + a["href"]
    title=a.string
    news={
        "link":link,
        "title":title
        }
    new_list.append(news)
    print(news)
    
pyexcel.save_as(records=new_list, dest_file_name="your_file.xlsx")

