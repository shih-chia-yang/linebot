#flask

- 免費網站框架
- 內建伺服器和偵錯器
    - 本身建置伺服器，不須將網頁程式上傳至外部網頁伺服器，只需啟動內建伺服器即可觀看網頁
- 功能強大的偵錯器
    - flask伺服器具備偵錯工具，且預設處於偵錯狀態，若執行時發生錯誤，會自動將錯誤資訊傳送給用戶端
- 使用unicode編碼
    - flask預設自動加入utf-8編碼格式的http head
- 使用jinja2模板(Template)
    - 由Django template發展而來，效能比Django更好，可製作更豐富多元的網頁
- 可與python單元測試緊密結合
    - flask提供了test_client函式測試介面，可與python付帶的單元測試架構unitest緊密結合，提供驗證