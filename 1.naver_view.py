import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 User-Agent 값 가져오기
user_agent = os.getenv("USER_AGENT")

# headers 딕셔너리에 User-Agent 적용
headers = {
    "User-Agent": user_agent
}

base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
#print(url)

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