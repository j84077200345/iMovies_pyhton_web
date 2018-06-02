import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.imovie4u.com/?s=%E6%AD%BB%E6%81%832")
content = request.content
soup = BeautifulSoup(content, "html.parser")

link = soup.find_all('div', {"class": "result-item"})

if not link:
    no_result = soup.find('h2')
    print(no_result.text)
else:
    for element in link:
        _link = element.find('a')
        movie_link = _link.get("href")


req = requests.get("http://www.movieffm.com/2018/02/ColdSkin.html")
con = req.content
soup2 = BeautifulSoup(con, "html.parser")

watch = soup2.find('iframe')
watch_link = watch.get("src")
print(watch_link)

detail = soup2.find_all('div', {"class": "separator"})
for el in detail:
    print(el.text)
