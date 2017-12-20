import requests
from pymongo import MongoClient

#要抓的網址
REST_EU_ROOT_URL = 'http://restcountries.eu/rest/v1'

#連mongodb , cmd先到mongodb的位置,執行server => mongod.exe --dbpath c:\mongodb\data
def get_mongo_database(db_name, host='localhost',port=27017,username=None,password=None):
    if username and password:
        mongo_uri='mongodb://%s:%s@%s/%s'%(username,password,host,db_name)
        conn=MongoClient(mongo_uri)
    else:
        conn=MongoClient(host,port)
    return conn[db_name]

#確定狀況後 , 抓資料
def REST_country_request(field='all',name=None,params=None):
    headers = {'User-Agent':'Mozilla/5.0'}
    if not params:
        params={}
    if field == 'all':
        return requests.get(REST_EU_ROOT_URL+'/all')
    
    url = '%s/%s/%s'%(REST_EU_ROOT_URL, field, name)
    print('URL : '+url)
    response=requests.get(url,params=params,headers=headers)
    
    if not response.status_code == 200:
        raise Exception('Request failed with status code '+ str(response.status_code))
    return response
    
#response = REST_country_request('currency','usd')
#print(response.text)

db_nobel = get_mongo_database('nobel_prize')
col = db_nobel['country_data']
   
#response = REST_country_request()
#col.insert_many(response.json())

print(list(col.find({'name':{'$in':['Syria','Taiwan']}})))
#print(list(col.find({'currencies':{'$in':['USD']}})))
#print(list(col.find({'currencies':{'$in':['TWD']}})))