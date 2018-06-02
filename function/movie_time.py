import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.imovie4u.com/?s=%E5%8B%95%E4%BD%9C")
content = request.content
soup = BeautifulSoup(content, "html.parser")

time = soup.find_all('div', {"class": "result-item"})

if not time:
    no_result = soup.find('h2')
    print(no_result.text)
else:
    for element in time:
        _link = element.find('span', {"class": "year"})
        movie_link = _link.text
        print(movie_link)
