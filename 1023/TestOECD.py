import requests

response= requests.get('http://stats.oecd.org/sdmx-json/data/QNA/AUS+AUT.GDP+B1_GE.CUR+VOBARSA.Q/all?startTime=2009-Q2&endTime=2011-Q4')
if response.status_code == 200 : #連線正常
    data=response.json()
    print (data.keys())