from pymongo import MongoClient
#常數區域#
DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS   = 'winners'
##########

#拿mongo的資料庫
def get_mongo_database(db_name, host='localhost',port=27017,username=None,password=None):
    if username and password:
        mongo_uri='mongodb://%s:%s@%s/%s'%(username,password,host,db_name)
        conn=MongoClient(mongo_uri)
    else:
        conn=MongoClient(host,port)
    return conn[db_name]

#mongo格式轉dicts
def mongo_coll_to_dicts(dbname='test',collname='test',query={},del_id=True,**kw):
    db = get_mongo_database(dbname,**kw)
    #刪、改
    db[collname].remove({'name':'Albert Einstein'})
    db[collname].update({'name':'Marie Curie','year': 1911},{'category': 'Chemistry', 'name': 'Marie Curie', 'nationality': 'Polish', 'sex': 'female', 'year': 1990},{'multi': 'true'})
    
    res=list(db[collname].find(query))
    if del_id:
        for r in res:
            r.pop('_id')
            #pop() 將會移除list 中最後的項目並回傳它
    return res

#print(mongo_coll_to_dicts(DB_NOBEL_PRIZE,COLL_WINNERS,{'year':{'$gt':1930}})) #只查印出大於1930
print(mongo_coll_to_dicts(DB_NOBEL_PRIZE,COLL_WINNERS))