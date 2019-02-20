from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")

with open("www.apple", "wb") as f:
    f.write(raw_data)

soup = BeautifulSoup(page_content, "html.parser")
ul=soup.find("ul","")

li_list = ul.find_all("li")


new_list=[]
for li in li_list:
    h3=li.h3
    a=h3.a
    title=a.string
    h4=li.h4
    a=h4.a
    title2=a.string
    news={
        "title":title,
        "title2":title2
        }
    new_list.append(news)
    #print(news)
    
pyexcel.save_as(records=new_list, dest_file_name="your_file.xlsx")

#download
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 100, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)

for i in new_list:
    name=i["title"]
    dl.download([name])
    a+=1
