import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.imovie4u.com/?s=%E6%AD%BB%E6%81%832")
content = request.content
soup = BeautifulSoup(content, "html.parser")

title = soup.find_all('div', {"class": "result-item"})

if not title:
    no_result = soup.find('h2')
    print(no_result.text)
else:
    for element in title:
        movie_title = element.find('div', {"class": "title"})
        print(movie_title.text)
