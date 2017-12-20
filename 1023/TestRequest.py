import requests

#response = requests.get('https://zh.wikipedia.org/wiki/%E8%AB%BE%E8%B2%9D%E7%88%BE%E7%8D%8E%E5%BE%97%E4%B8%BB%E5%88%97%E8%A1%A8')
#print(response.status_code) #取得回應訊息的狀態碼
#print(dir(response))        #顯示目錄中的檔案和子目錄清單
#print(response.text)        #內容

response= requests.get('http://opendata2.epa.gov.tw/AQX.json')
print(response.status_code)
data=response.json()
print(data[0].keys()) 

for d in data:
    if(d['County'] in ['新竹市','新竹縣','苗栗縣','雲林縣','臺南市']):
        print('縣市:',d['County'],end='\t')
        print('地點:',d['SiteName'],end='\t')
        print('PM2.5:',d['PM2.5'],end='\t')
        print('空氣品質:',d['Status'])
