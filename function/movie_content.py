import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.imovie4u.com/?s=%E5%8B%95%E4%BD%9C")
content = request.content
soup = BeautifulSoup(content, "html.parser")

con = soup.find_all('div', {"class": "result-item"})

if not con:
    no_result = soup.find('h2')
    print(no_result.text)
else:
    for element in con:
        movie_content = element.find('div', {"class": "contenido"})
        print(movie_content.text)
