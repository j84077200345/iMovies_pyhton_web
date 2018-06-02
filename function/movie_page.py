import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.imovie4u.com/genre/action/")
content = request.content
soup = BeautifulSoup(content, "html.parser")

page = {}
for _page in soup.find_all('div', {"class": "pagination"}):
    page_value = _page.find('a', {"class": "inactive"})
    page['{}'.format(page_value.text)] = page_value.get("href")

print(page)
