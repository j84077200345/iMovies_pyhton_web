import requests
from bs4 import BeautifulSoup


def find_search_content(search):
    request = requests.get("https://www.imovie4u.com/?s={}".format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")

    return soup

def find_home_content(home):
    request = requests.get("{}".format(home))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")

    return soup

def find_page_content(page):
    request = requests.get(page)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")

    return soup

def find_movie(soup, all_movie, i=1):
    result = soup.find_all('div', {"class": "result-item"})
    if not result:
        no_result = soup.find('h2')
        all_movie[i] = no_result.text
    else:
        for element in result:
            _title = element.find('div', {"class": "title"})
            movie_title = _title.text
            _link = element.find('a')
            movie_link = _link.get("href")
            _img = element.find('div', {"class": "image"})
            __img = _img.find('img')
            movie_img = __img.get("src")
            _content = element.find('div', {"class": "contenido"})
            movie_content = _content.text

            # request = requests.get(movie_link)
            # content = request.content
            # watch_soup = BeautifulSoup(content, "html.parser")
            # watch = watch_soup.find('iframe')
            # watch_link = watch.get("src")

            all_movie['{}'.format(i)] = {"title": movie_title, "link": movie_link, "img": movie_img,
                                         "content": movie_content}
            i = i + 1

    return all_movie


def movie_time(soup, all_movie, i=1):
    time = soup.find_all('div', {"class": "result-item"})
    if not time:
        no_result = soup.find('h2')
        all_movie[i] = no_result.text
    else:
        for element in time:
            _time = element.find('span', {"class": "year"})
            movie_time = _time.text
            all_movie.get('{}'.format(i))['time'] = movie_time
            i = i + 1

    return all_movie


def find_home_movie(soup):
    all_movie = {}
    i = 1
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
        time = _time.text
        movie_content = _content.text

        all_movie['{}'.format(i)] = {"title": movie_title, "link": movie_link, "img": movie_img, "time": time,
                                     "content": movie_content}
        i = i + 1

    return all_movie

def every_movie(soup):
    all_movie = {}
    find_movie(soup, all_movie, i=1)
    movie_time(soup, all_movie, i=1)

    return all_movie

def watch_movie(movie_link):
    request = requests.get(movie_link)
    content = request.content
    watch_soup = BeautifulSoup(content, "html.parser")
    watch = watch_soup.find('iframe')
    watch_link = watch.get("src")
    return watch_link

def page_bar():
    page = {}
    for p in range(1, 21):
        page['{}'.format(p)] = "https://www.imovie4u.com/movies/page/{}/".format(p)
    return page

