from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://en.wikipedia.org'
HEADERS  = {'User-Agent':'Mozilla/5.0'} #告訴網站，我們是一個正常的瀏覽器在給它發送資訊，請它給我們資料

#拿那網址的資料，lxml是一種解析器
def get_Nobel_soup():
    response = requests.get(BASE_URL + '/wiki/List_of_Nobel_laureates' ,headers=HEADERS)
    return BeautifulSoup(response.content,'lxml')
#從 tr 找出 th , 有 link 印出欄名、網址，沒有 link 印出欄名就好
def get_column_titles(table):
    cols = []
    for th in table.select_one('tr').select('th')[0:]:
        link = th.select_one('a') # href 前面會有 a 來指定超連結目標
        if link:
            cols.append({'name':link.text,'href':link.attrs['href']})
        else:
            cols.append({'name':th.text  ,'href':None})
    return cols
    
soup     = get_Nobel_soup()

#版1 print(soup.find('table',{'class':'wikitable sortable'}))
#版2 print(soup.select('table.wikitable.sortable'))
#版3 用select找出table,用th找出表格的欄名
#print(soup.select_one('table.wikitable.sortable').select('th'))
print(get_column_titles(soup))