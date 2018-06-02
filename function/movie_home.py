import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.imovie4u.com/movies/")
content = request.content
soup = BeautifulSoup(content, "html.parser")

title = soup.find_all('article', {"class": "item movies"})
for element in title:
    _title = element.find('h3')
    _link = element.find('a')
    _img = element.find('img')
    _time = element.find('span', {"class": False})
    _content = element.find('div', {"class": "texto"})
    movie_title = _title.text
    movie_link = _link.get("href")
    movie_img = _img.get("src")
    movie_time = _time.text
    movie_content = _content.text

    print(movie_title)
    print(movie_link)
    print(movie_img)
    print(movie_time)
    print(movie_content)
