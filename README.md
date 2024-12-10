資料庫管理
B11705007 袁詠宸
B11705017 陳芃宇
B11705024 謝友毅

專案簡介

使用者功能
User
Publisher

使用方法
使用備份檔 database_with_fake_data 加上 .backup 之後，復原資料庫
預設連線通道為 http://127.0.0.1:5000，可至 client.py 修改
在 server.py 的 get_connection() 設定資料庫名稱 (dbname)、使用者名稱 (user)、資料庫密碼 (password)及主機位置 (host)

先執行server.py啟動伺服器
python .\server.py

再透過 client.py 向伺服器連線：
python .\client.py 

技術細節

程式說明

開發環境
Windows 11
Python 3.11.9
    
PostgreSQL: 16.4
