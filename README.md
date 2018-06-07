# iMovies_pyhton_web  
### 這是一個使用python爬蟲和Flask框架所撰寫成的線上免費電影網站
----------------------------------------------------------------
## Pyhton Web 開發 (使用PyCharm IDE)
架構： 使用 Pyhton web Framework => Flask  
1.     Front-end: Bootstrap CSS Framework  
2.     Back-end: Pyhton web crawler  
----------------------------------------------------------------
## 專案類別圖
* Method => Find web content, Find title, Find link, Find img, Find content  
* Video => title, link, img, `Favorite()`, `Delete()`  
* User => Account(Only one), Password, Name  
-----------------------------------------------------------------  
## Step 1:  
New Project --> iMovies --> Using virtualenv 命名為Library (虛擬開發環境是為了避免不同專案import 套件時重複或搞混)  
> Project Directory:  
> * iMovies  
>   * common folder (放連接MongoDB的Code)  
>   * fuction folder (放Crawler Testing Code)  
>   * modules folder (放 item, user, video class) 
>   * static folder  
>     * css    
>     * img   
>     * js  
>   * templates folder (放html顯示頁面)
>   * run.py (主程式)
>   * .gitignore
>   * Procfile
>   * requirements.txt
>   * runtime.txt  
static 和 templates folder 是 Flask API 預設參考到的資料夾  
----------------------------------------------------------------
## Step 2:  
function => 爬蟲程式重點 (最後要把不同的爬蟲整合在一個item.py module內)  
* soup.find_all() => return list => 要用for loop查找裡面內容  
* element.get('attribute') => 取出html tag內特定數屬性  
* re.findall(".....[\S]+", data_source) => re是正規化表示法, \S為非空白字元 => return 資料來源的型態
* check 是否為empty list => if not list_name:  
* "~".split() => return list  
* dictionary {} => page['key'] = value  
* all_movie.get('key') 或 all_movie['key'] => 均為取出dict中的key值
----------------------------------------------------------------
## Step 3:  
搭配Bootstrap建立基底頁面  
* 利用Jinja語法引用bootstrap core CSS => {% include "html_reference.html" %}  
* 另外custom CSS需額外寫入html_reference中 => <link rel="stylesheet" href="{{url_for('static', filename='css/style.css')}}">  
* Search的參數傳遞：(使用http GET方式)
  * base.html
  ```
  <form class="form-inline mt-2 mt-md-0" action="/result">
     <input class="form-control mr-sm-2" type="text" placeholder="Only Chinese Search..." aria-label="Search" name="search" required>
     /*透過request.args.get('search')來取得input value*/   
        <button class="btn btn-outline-warning my-2 my-sm-0" type="submit">
           <i class="fas fa-search"></i>&nbsp;Search
        </button>
  </form>
  ```  
  * result.html
  ```
  {% extends "base.html" %}
  {% block content %}
     要替換的內容
  {% endblock %}
  ```  
* 其他過程省略
----------------------------------------------------------------
## Step 4:  
* 連接MongoDB:  
  * 本地端 => mongod.exe, mongo.exe  
  * mlab(遠端) => 便於之後將專案上傳到Heroku  

* 主要連接Code:  
  * ```client = pymongo.MongoClient(["mongodb://j84077200345:jack6114@ds139920.mlab.com:39920/movies"])```
  * ```DATABASE = client['movies'] (連接DB的名稱)```
  * ```DATABASE['users'].insert({'key': 'value'}) (對特定collection進行存取)```  

* 建立Database class:  
  * database.py
  ```
  class Database(object):
      URI = ["mongodb://j84077200345:jack6114@ds139920.mlab.com:39920/movies"]
      DATABASE = None

      @staticmethod
      def initialize():
          client = pymongo.MongoClient(Database.URI)
          Database.DATABASE = client['movies']

      @staticmethod
      def insert(collection, data):
          Database.DATABASE[collection].insert(data)

      @staticmethod
      def find(collection, query):
          return Database.DATABASE[collection].find(query)

      @staticmethod
      def find_one(collection, query):
          return Database.DATABASE[collection].find_one(query)

      @staticmethod
      def remove(collection, query):
          Database.DATABASE[collection].remove(query)
  ```  

* 建立User class:
  * user.py
     ``` 
     class User(object):
         def __init__(self, name, account, password):
             self.name = name
             self.account = account
             self.password = password

         @staticmethod
         def is_login_valid(account, password):
             user_data = Database.find_one(collection='users', query={"Account": account})
             if user_data is None:
                 return False
             if user_data['Password'] != password:
                 return False
             return True

         @staticmethod
         def register_user(name, account, password):
             user_data = Database.find_one(collection='users', query={"Account": account})
             if user_data is not None:
                 return False
             User(name, account, password).save_to_db()
             return True

         def save_to_db(self):
             Database.insert(collection='users', data=self.json())

         def json(self):
             return {
                 "Name": self.name,
                 "Account": self.account,
                 "Password": self.password
             }

         @staticmethod
         def find_user_data(account):
             user_data = Database.find_one(collection='users', query={"Account": account})
             return user_data
     ``` 
* 補充：
  * __init__用來定義instance建立後的初始化動作 => 第1個參數self代表建立的類別實例
  * 每個instance建立後有自己的資料狀態，可透過 . 來存取屬性和方法
  * Python中instance可操作屬性和方法(instance method)，方法中的第1個參數self作為接受instance的參考
  * @staticmethod就像是一個function，只是剛好被定義在class裡而不是module level => item.py裡的method即是一個function定義在module level
-------------------------------------------------------------
## Step 5:  
* Login Page (login.html): 注意要設定app.secret_key="..."
  * run.py
  ```
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
  ```
  ```
  @app.before_first_request
  def init_db():
    Database.initialize()
    session['account'] = session.get('account')
    session['name'] = session.get('name')
  ```
-----------------------------------------------------------
## Step 6:  
* Logout Page (logout.html):  
  * run.py
  ```
  @app.route("/logout")
  def logout_method():
    session['account'] = None
    return redirect("/")
    /*home.html => 要新增判斷式*/
  ```
-----------------------------------------------------------
## Step 7:  
* Register Page (register.html):  
  * user.py 新增
  ```
  @staticmethod
    def register_user(name, account, password):
        user_data = Database.find_one(collection='users', query={"Account": account})
        if user_data is not None:
            return False
        User(name, account, password).save_to_db()
        return True
  ```
  * run.py  
  ```
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
  ```
-------------------------------------------------------
## Step 8:  
* Favorite Page (favorite.hmtl): 含加入功能和刪除功能
  * 建立Video class (video.py):  
  ```
  class Video(object):
    def __init__(self, account, title, link, img):
        self.account = account
        self.title = title
        self.link = link
        self.img = img

    def save_to_db(self):
        Database.insert(collection='videos', data=self.json())

    def json(self):
        return {
            "Account": self.account,
            "Title": self.title,
            "Link": self.link,
            "Img": self.img
        }

    @staticmethod
    def find_video(account):
        user_video = Database.find(collection='videos', query={"Account": account})
        return user_video

    @staticmethod
    def delete_video(account, link):
        Database.remove(collection='videos', query={"Account": account, "Link": link})
  ```
  * run.py
  ```
  @app.route("/favorite", methods=['GET','POST'])
  def favorite_method():
    if session['account']:
        if request.method == 'POST':
            url = request.form['url']  /*app.route("/result")要新增 url=request.url*/
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
  ```
  * result.html新增Favorite button
  ```
  <form style="display: inline-block;" action="/favorite" method="post">
            <input type="hidden" name="url" value="{{url}}">
            <input type="hidden" name="title" value="{{all_movie.get('{}'.format(movie))['title']}}">
            <input type="hidden" name="link" value="{{all_movie.get('{}'.format(movie))['link']}}">
            <input type="hidden" name="img" value="{{all_movie.get('{}'.format(movie))['img']}}">
            <button style="position: relative; top:7px;" class="btn btn-outline-danger btn-sm" type="submit">
                <i class="far fa-heart"></i>&nbsp;Favorite
            </button>
  </form>
  ```
  * favorite.html
  ```
  {% for video in user_video %}
    改成{{ video.Link }}
  {% endfor %}
  ```
  * 刪除功能 (run.py)  
  ```
  @app.route("/delete", methods=['POST'])
  def delete_method():
     link = request.form['link']
     account = session['account']
     Video.delete_video(account, link)
     return redirect("/favorite")
  ```
  * favorite.html 新增
  ```
  <form action="/delete" method="post" style="display: inline-block;">
            <input type="hidden" name="link" value="{{video.Link}}">
            <button style="position: relative; top:7px;" class="btn btn-outline-dark btn-sm" type="submit">
                <i class="far fa-trash-alt"></i>&nbsp;Delete
            </button>
  </form>
  ```
  * 避免重複加入我的最愛 (run.py)  
  在result_page()中新增  
  ```
  favorite_video = []
    user_favorite = Video.find_video(session['account'])
    for video in user_favorite:
        favorite_video.append(video['Link'])
  ```
  result.html => 加判斷式判斷使用者是否登入，並check其最愛的內容
  ```
  {% if session['account'] %}
        {% if "{}".format(all_movie.get('{}'.format(movie))['link']) in favorite_video %}
        <form style="display: inline-block;">
            <button style="position: relative; top:7px;" disabled class="btn btn-outline-secondary btn-sm"
                    type="button"><i class="fas fa-plus"></i>&nbsp;Added
            </button>
        </form>
        {% endif %}
        {% if "{}".format(all_movie.get('{}'.format(movie))['link']) not in favorite_video %}
        <form style="display: inline-block;" action="/favorite" method="post">
            <input type="hidden" name="url" value="{{url}}">
            <input type="hidden" name="title" value="{{all_movie.get('{}'.format(movie))['title']}}">
            <input type="hidden" name="link" value="{{all_movie.get('{}'.format(movie))['link']}}">
            <input type="hidden" name="img" value="{{all_movie.get('{}'.format(movie))['img']}}">
            <button style="position: relative; top:7px;" class="btn btn-outline-danger btn-sm" type="submit">
                <i class="far fa-heart"></i>&nbsp;Favorite
            </button>
        </form>
        {% endif %}
  {% endif %}
  ```
  -----------------------------------------------------------
  ## Step 9:  
  * upload to Heroku: 新建4個file
    1. .gitignore => library (告訴Heroku要使用的環境)
    2. Procfile => web:  gunicorn run:app
    3. requirements.txt => (告訴Heroku要install的套件)
    4. runtime.txt => python-3.6.4 (告訴Heroku要使用的python版本)  
