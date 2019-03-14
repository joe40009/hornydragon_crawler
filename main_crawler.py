from urllib.request import urlopen
from bs4 import BeautifulSoup
import hornydragon_crawler

url = 'https://hornydragon.blogspot.com/search/label/%E9%9B%9C%E4%B8%83%E9%9B%9C%E5%85%AB%E7%9F%AD%E7%AF' \
      '%87%E6%BC%AB%E7%95%AB%E7%BF%BB%E8%AD%AF?updated-max=2019-01-25T19%3A45%3A00%2B08%3A00&max-results=30#PageNo=2'

response = urlopen(url)
html = BeautifulSoup(response)

hdhis = html.find_all("div", class_="post-outer")
ppp = str(hdhis).split('"')

for i in range(1, 31):
    print(ppp[4*i-1])
    hornydragon_crawler.urls(ppp[4*i-1])

