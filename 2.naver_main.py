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

url = "https://www.naver.com/"

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

