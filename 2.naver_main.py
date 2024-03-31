import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36s"
}

req = requests.get(url, headers=headers)

#print(req.request.headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

print(soup.h1)
print()

h1 = soup.find('h1')
print(h1)
print()

h2 = soup.find(class_="search_logo")
print(h2)
print()

#이거 이제는 안되는듯
h3 = soup.find(class_="blind", sring="검색")
print(h3)

