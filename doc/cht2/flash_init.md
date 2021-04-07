#flask_init

- 基本架構
```python
#匯入flask，建立flask物件
import flask import Flask
app=Flask(__name__)

...route1
...route2

#執行flask程式
if __name__=='__main__':
    app.run()
```

- 建立route
```python
#decorator，將網址與函式結合
#url 為網頁路徑，設為/，則表示http://127.0.0.1:5000
#設為/url ，位址為 http://127.0.0.1:5000/url
# function name通常會與網頁路徑同名
@app.route('url')
def function_name():
    process
```

- 多網址對應相同函式
```python
@app.route('url1')
@app.route('url2')
def function():
    process

```

- app.run()參數
    1. host :設定伺服器服務的位址，預設值為127.0.0.1,設定為0.0.0.0表示無論本地位址或真實位址都能連上flask伺服器
    2. port :設定埠號
    3. debug :設定是否顯示錯誤訊息      
```python
app.run(host='0.0.0.0',port=80,debug=false)

```

- 建立動態路由，路由傳遞參數

|資料型態|說明|
|--|--|
|string|可輸入任何字串，此為預設值|
|int|可輸入整數|
|float|可輸入浮點數|
|path|可輸入包含/字元的路徑名稱|

```python
#傳遞字串型態參數 name到about網址
@app.route('/about/<string:name>')
def about(name):
    process

```