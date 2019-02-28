from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
import json

a=input()
url="https://wind.waqi.info/nsearch/full/"+a+"?n=4"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")

page_content2=json.loads(page_content)
re=page_content2["results"]
print("aqi:",re[0]["s"]["a"])
print("time:",*re[0]["s"]["t"])

