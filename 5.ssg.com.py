import requests
from bs4 import BeautifulSoup

url = "https://ssg.com/event/eventMain.ssg"

headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36s"
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