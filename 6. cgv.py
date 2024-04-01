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

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
req = requests.get(url, headers=headers)
html = req.text
soup = BeautifulSoup(html, "html.parser")

sect_movie_chart = soup.select_one(".sect-movie-chart")

movie_chart = sect_movie_chart.select("li")

for rank, movie in enumerate(movie_chart, 1):
    #기존은 for movie in movie_chart 랭크 1등부터 표시하게 하기위해 수정
    title = movie.select_one(".title")
    score = movie.select_one(".score")
    ticketing = score.select_one(".percent")
    egg_gage = score.select_one(".egg-gage.small > .percent")
    #원랜 egg-gage small인데 스페이스바는 모두 .으로 변경
    #egg-gage small 내의 percent 태그라는 뜻
    info = movie.select_one(".txt-info > strong").next_element
    ''' 
    아래의 태그에서 strong 다음 요소인 2024.04.10만 가져옴
    왜냐면 출력시 span 태그가 나오면서 .strip()을써도 정리가 안됨
    개봉이라는 단어는 모든 요소에 존재하기때문에 아래 출력만 따로 해주게함
    <span class="txt-info">
        <strong>
            2024.04.10 
            <span>개봉</span>
            <em class="dday">D-9</em>
        </strong>
    </span>
    '''
    print(f"<<<<{rank}위>>>>")
    print(title.text)
    print(ticketing.get_text(" : "))
    #티케팅의 모든 텍스트가 출력되면서 예매율98%이런식으로 저장되서 예매율 : 98%이런 방식으로 저장하는 방법
    print(egg_gage.text)
    print(f"{info.strip()} 개봉")
    #스트립으로 정리후 개봉은 따로 출력
    print()