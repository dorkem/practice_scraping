import requests
from bs4 import BeautifulSoup

url = "https://news.daum.net/"

headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36s"
}

req = requests.get(url, headers=headers)

#print(req.request.headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

item_issue = soup.select(".item_issue")

for item in item_issue:
# 다음뉴스의 출판사는 사진으로 되어있고 alt태그 내에 출판사의 이름이 표시되어있음
    # press = item.select(".thumb_g")[1]["alt"]
    press = item.select_one(".logo_cp > img")["alt"]
    category = item.select_one(".txt_category").text
    link_txt = item.select_one(".link_txt")
    link = link_txt["href"]
    txt = link_txt.text.strip()
    print(f"{press} - {category}")
    print(f"{txt} : {link}")
    print()
