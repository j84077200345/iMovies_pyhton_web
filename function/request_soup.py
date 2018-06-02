import requests
from bs4 import BeautifulSoup

# request = requests.get("https://www.imovie4u.com/movies/page/7/")
# content = request.content
# soup = BeautifulSoup(content, "html.parser")

watch_content = {}
i = 1
request = requests.get("http://www.movieffm.com/2018/02/bd-inception.html")
content = request.content
watch_soup = BeautifulSoup(content, "html.parser")
detail = watch_soup.find_all('div', {"class": "separator"})
for element in detail:
    if element.text == "\n":
        continue
    watch_content[i] = element.text
    i = i + 1

print(watch_content)
