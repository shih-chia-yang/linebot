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

- 用get傳遞參數，`@app.route('\url',methods=['GET'])`
    - 接收get參數，匯入request模組。from flask import request
    - request.args.get('arg name')

```python
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    name=request.args.get('name')
    return f' hello {name}'
```

> [!TIP]
> 匯入request 模組
> 以GET方式建立route
> 取得GET方式傳送的參數值並賦值
> 進行處理與返回結果
> 函式不需增加參數

- post 傳遞參數
```python
@app.route('url',methods=['GET','POST'])
```
- 取得post參數
```python
from flask import request

request.values('<arg name>')
```

- 使用template
flask 提供template功能，可以直接顯示html content 簡化產生網頁的工作

1. 匯入render_template
```python
form flask import render_template
```

2. 讀取網頁檔案
```python
render_template('網頁檔案名稱')
```

3. flask的網頁檔案需放在flask程式路徑的templates資料夾中，系統才能讀取


- 傳送參數及變數給網頁檔案

1. 在route設定參數
```python
@app.route('/url/<string:name>')

```

2. 在render_template加入第二個參數
```python
#**locals() 指傳送所有參數與區域變數
render_template('html filename',**locals())
```

3. 網頁中接收參數的方法是將參數名稱以{{`variable`}}包起來