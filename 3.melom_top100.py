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

def get_song_nums(song_num_text):
    # song_num = []
    # for num in song_num_text:
    #     if num.isdigit():
    #         song_num.append(num)
    song_num = "".join([num for num in song_num_text if num.isdigit()])        
    # song_num="".join(song_num)
    
    return song_num

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=headers)
html = req.text

soup = BeautifulSoup(html, "html.parser")

'''lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
lst = lst50+lst100'''

lst = soup.select(".lst50, .lst100")


for rank,i in enumerate(lst, 1):
    title = i.select_one(".ellipsis.rank01 a")

    singer = i.select_one(".ellipsis.rank02 a")
    singer_link = get_song_nums(singer["href"])
    
    album = i.select_one(".ellipsis.rank03 a")
    album_link = get_song_nums(album["href"])

    #ellipsis.rank class 아래에 하위에 위치한 a태그
   
    print(f"{rank} : {title.text}")
    print(f"{singer.text} : https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"{album.text} : https://www.melon.com/album/detail.htm?albumId={album_link}")

    #랭크 = 1부터 lst까지 순서대로