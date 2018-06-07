# iMovies_pyhton_web
## 這是一個使用python爬蟲和Flask框架所撰寫成的線上免費電影網站
----------------------------------------------------------------
## Pyhton Web 開發 (使用PyCharm IDE)
架構： 使用 Pyhton web Framework => Flask  
1.     Front-end: Bootstrap CSS Framework  
2.     Back-end: Pyhton web crawler  
----------------------------------------------------------------
## 專案類別圖
> Method => Find web content, Find title, Find link, Find img, Find content  
> Video => title, link, img, Favorite(), Delete()  
> User => Account(Only one), Password, Name
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
* re.findall(".....[\S]+", data_source) => return 資料來源的型態
