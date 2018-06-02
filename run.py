from flask import Flask, render_template, request, session, redirect
from modules import item
from modules.user import User
from modules.video import Video
from common.database import Database

app = Flask(__name__)
app.secret_key = "jack6114"

@app.before_first_request
def init_db():
    Database.initialize()
    session['account'] = None
    session['name'] = None

@app.route("/")
def hello():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])

    home = "https://www.imovie4u.com/movies/"
    soup = item.find_home_content(home)
    all_movie = item.find_home_movie(soup)
    all_page = item.page_bar()

    return render_template("home.html", all_movie=all_movie, url=url, favorite_video=favorite_video, all_page=all_page)

@app.route("/home_page", methods=['POST'])
def home_page():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])

    page = request.form['page']
    soup = item.find_page_content(page)
    all_movie = item.find_home_movie(soup)
    all_page = item.page_bar()

    return render_template("home.html", all_movie=all_movie, url=url, favorite_video=favorite_video, all_page=all_page)

@app.route("/login", methods=['GET', 'POST'])
def login_method():
    if request.method == 'POST':
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        check = User.is_login_valid(account, password)
        if check is True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('Name')
            return redirect("/")
        else:
            message = "Ur account or password is wrong !!"
            return render_template('login.html', message=message)
    else:
        return render_template('login.html')

@app.route("/logout")
def logout_method():
    session['account'] = None
    return redirect("/")

@app.route("/register", methods=['GET', 'POST'])
def register_method():
    if request.method == 'POST':
        name = request.form['InputName']
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        result = User.register_user(name, account, password)
        if result is True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('Name')
            return redirect("/")
        else:
            message = "Ur account is already existed !!"
            return render_template('register.html', message=message)
    else:
        return render_template('register.html')

@app.route("/result")
def result_page():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])
    search = request.args.get('search')
    soup = item.find_search_content(search)
    all_movie = item.every_movie(soup)

    return render_template("result.html", result=search, all_movie=all_movie, url=url, favorite_video=favorite_video)

@app.route("/favorite", methods=['GET','POST'])
def favorite_method():
    if session['account']:
        if request.method == 'POST':
            url = request.form['url']
            title = request.form['title']
            link = request.form['link']
            img = request.form['img']
            account = session['account']
            Video(account, title, link, img).save_to_db()
            return redirect(url)
        else:
            account = session['account']
            user_video = Video.find_video(account)
            return render_template("favorite.html", user_video=user_video)
    else:
        return redirect("/login")

@app.route("/delete", methods=['POST'])
def delete_method():
    link = request.form['link']
    account = session['account']
    Video.delete_video(account, link)
    return redirect("/favorite")

@app.route("/watch", methods=['POST'])
def watch_page():
    watch = request.form['watch']
    watch_link = item.watch_movie(watch)
    watch_title = request.form['watch_title']
    return render_template("watch.html", watch_link=watch_link, watch_detail=watch_title)

@app.route("/category/action", methods=['GET'])
def category_action():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])

    category = "https://www.imovie4u.com/genre/action/"
    soup = item.find_home_content(category)
    all_movie = item.find_home_movie(soup)

    return render_template("category.html", all_movie=all_movie, url=url, favorite_video=favorite_video)

@app.route("/category/drama", methods=['GET'])
def category_drama():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])

    category = "https://www.imovie4u.com/genre/drama/"
    soup = item.find_home_content(category)
    all_movie = item.find_home_movie(soup)

    return render_template("category.html", all_movie=all_movie, url=url, favorite_video=favorite_video)

@app.route("/category/fantasy", methods=['GET'])
def category_fantasy():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])

    category = "https://www.imovie4u.com/genre/fantasy/"
    soup = item.find_home_content(category)
    all_movie = item.find_home_movie(soup)

    return render_template("category.html", all_movie=all_movie, url=url, favorite_video=favorite_video)

@app.route("/category/comedy", methods=['GET'])
def category_comedy():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])

    category = "https://www.imovie4u.com/genre/comedy/"
    soup = item.find_home_content(category)
    all_movie = item.find_home_movie(soup)

    return render_template("category.html", all_movie=all_movie, url=url, favorite_video=favorite_video)

@app.route("/category/horror", methods=['GET'])
def category_method():
    url = request.url
    favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])

    category = "https://www.imovie4u.com/genre/horror/"
    soup = item.find_home_content(category)
    all_movie = item.find_home_movie(soup)

    return render_template("category.html", all_movie=all_movie, url=url, favorite_video=favorite_video)

if __name__ == "__main__":
    app.run(debug=True, port=5010)
