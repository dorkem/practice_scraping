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

url = "https://www.coupang.com/np/search?component=&q="
keyword = input("검색할 상품을 입력하세요 : ")
search_url = url + keyword

cookie = {"a":"b"} #이런거 안하고 셀레니움하면 되긴한데 뷰티풀숩만 사용하는게 빨라서 좋긴함
req = requests.get(search_url, timeout=5, headers=headers, cookies=cookie)
#timeout 5초주고 응답대기함 -> 근데 쿠팡은 useragent말고 뭔가 더 요구함 바로 출력안해준다.
#서버에서 통신하는 데이터를 내 컴퓨터에서 주고받게 하는 것 : 쿠키 => 브라우저마다 다름


html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")
#.search-product이러면 ['search-product', 'sdw-aging-carousel-item'] 이런애들까지 다 나오니까 명시해놓음

rank = 0
for item in items:
    badge_rocket = item.select_one(".badge.rocket")
    if not badge_rocket:
        continue
    name = item.select_one(".name")
    price = item.select_one(".price-value")
    thumb = item.select_one(".search-product-wrap-img")
    link = item.a["href"]

    print(f"{rank}위")
    print(name.text.strip())
    print(f"{price.text}원")
    print(f"https://coupang.com{link}")
    #print(thumb["src"]) = 얘는 마지막으로 갈수록 이미지가 생성이 안된상태임
    if thumb.get("data-img-src"):
        imgurl = f"http:{thumb.get('data-img-src')}"
        print(imgurl) #get써야함 글고 이건 이미지 주소 링크임
    else :
        imgurl = f"http:{thumb['src']}"
        print(imgurl)
    print()

    img_req = requests.get(imgurl)
    with open(f"08_coupang/{rank}.jpg", "wb") as f:
        #text파일 할땐 w지만 바이너리 파일이라는 의미인 wb
        f.write(img_req.content)
    rank += 1