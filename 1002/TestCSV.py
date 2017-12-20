#python 讀入csv檔
#http://www.twse.com.tw/zh/page/trading/exchange/FMTQIK.html

import csv
with open('FMTQIK.csv',encoding='Big5') as f:  #打開檔案編碼是big5, 縮寫成f
    reader = csv.DictReader(f, fieldnames = ["日期","成交股數","成交金額","成交筆數","發行量加權股價指數","漲跌點數"])
    #讀為 dict 格式，各行名字為[]
    print('日期','\t\t','成交股數','\t','成交金額')
    #印出資料標題

#單純列出    
#    for row in csv.reader(f):
#        print(row)

    for row in list(reader)[2:-3]:             #取第2行之後、倒數3行之前的資料
        print(row["日期"],'\t\t',row["成交股數"],'\t',row["成交金額"])
        #印出資料