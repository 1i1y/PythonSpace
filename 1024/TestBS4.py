from bs4 import BeautifulSoup
import requests
import requests_cache #快取網頁

    #快取網頁 7200s
requests_cache.install_cache('nobel_pages',backend='sqlite', expire_after=7200

BASE_URL = 'https://en.wikipedia.org'
HEADERS = {'User-Agent':'Mozilla/5.0'} #意思:我們是正當的使用者

def get_Nobel_soup():
    #.get   得到
    response = requests.get(BASE_URL+'/wiki/List_of_Nobel_laureates', headers=HEADERS) 
    #'lxml' 一種解析器
    return BeautifulSoup(response.content, 'lxml')
 
#抓出獎名，年先不要 
def get_column_titles(table):
    # []    list
    cols = [] 
    #.select_one 找有一個('')
    for th in table.select_one('tr').select('th')[1:]: #[1:] 抓出獎名，年先不要 ; 第一個tr就是這個資料表了 
        link = th.select_one('a')
        #有連結給連結，沒連結給內容
        if link:
            cols.append({'name':link.text,'href':link.attrs['href']})
        else:
            cols.append({'name':th.text  ,'href':None})
    return cols


#找每年的得獎人
def get_Nobel_winners(table):
    cols = get_column_titles(table)
    winners = []
    for row in table.select('tr')[1:-1]: #[1:-1] -1 倒數一行前, 因為最後一行又是獎名
        if(row.select_one('td') != None and len(row.select_one('td').text) in [4,8]): # 找年， !None 是為了解決右上方有[]的
            year = int(row.select_one('td').text[0:4])
            for i,td in enumerate(row.select('td')[1:]): # enumerate 列舉，組成一個索引序列
                for winner in td.select('a'):
                    href = winner.attrs['href']          # attrs 屬性
                    if not href.startswith('#endnote'):  # '#endnote' 是右上方有[]的
                        winners.append({
                            'year':year,
                            'category':cols[i]['name'],
                            'name':winner.text,
                            'link':winner.attrs['href']
                        })
    return winners

soup = get_Nobel_soup()

print(get_column_titles(soup))
#print(get_Nobel_winners(soup))