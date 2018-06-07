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
