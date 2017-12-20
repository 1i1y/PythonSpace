import json
from datetime import date, datetime

#isoformat 轉時間序列
def json_serial(obj):
    if isinstance(obj,(datetime,date)):
        return obj.isoformat()
    raise TypeError('Type %s not serializable'% type(obj))

print(json.dumps(datetime.now(), default=json_serial))
#print(json.dumps(datatime.now().isoformat())  一行完成，但下次用還得再次執行


#def 陳述句
#default 不存在時的默認值