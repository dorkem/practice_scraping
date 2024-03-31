import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
#print(url)

headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36s"
}

req = requests.get(url, headers=headers)

#print(req.request.headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

areas = soup.select(".view_wrap")

rank_num = 1
for area in areas:
    ad = area.select_one(".link_ad")
    if ad:
        #print("광고입니다.")
        continue
    title = area.select_one(".title_link._cross_trigger")
    name = area.select_one(".name")
    print(f"<<<<{rank_num}>>>>")
    print(name.text)
    print(title.text)
    print(title['href'])
    print()

    rank_num += 1