#  python 內建資料庫用法
#  c.execute
#
#
#
#

import sqlite3
conn = sqlite3.connect('db.sqlite3') # 副檔名，開心就好~
c = conn.cursor()
#c.execute(''' Create Table MSG(ID　integer, Name text, MSG text)''')
#3個' + 3個' = 中間內容全包，不管什麼都讀的到
#create 完 先註解起來

#c.execute(''' Insert into MSG values(1,'Nick','Hello SQLite') ''') #新建資料
#c.execute(''' Insert into MSG values(2,'Alan','Hello SQLite') ''') #新建資料
c.execute(''' select * from MSG''')  # 查詢
#print ( c.fetchall() )               # 印:全部倒出 ∵cursor是依序倒出 ∴再次執行fetchall,cursor己在資料最下方,就讀不到要的資料漲了

#c.execute(''' select * from MSG Where Name ='Alan' ''') #刪除資料, "先"查詢所要刪的資料對不對後再刪除
#c.execute(''' Delete from MSG Where Name ='Alan' ''') #刪除資料
print ( c.fetchall() )     

conn.commit()                        # 提交
conn.close()                         # 記得關。一定要關