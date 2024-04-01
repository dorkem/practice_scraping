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

req = requests.get(url, headers=headers)
html = req.text
soup = BeautifulSoup(html, "html.parser")



evt_osmu_lst = soup.select_one(".evt_osmu_lst")

eo_link = evt_osmu_lst.select(".eo_link")
 
for unit in eo_link:
    link = unit["href"]
    if link.startswith("https"):
        print(link)
    else:
        print(f"https://www.ssg.com{link}")
        
    eo_in = unit.select_one(".eo_in")
    
    text_list = eo_in.find_all(string=True)
    for text in text_list:
        if text != "\n":
            print(text)
    print()