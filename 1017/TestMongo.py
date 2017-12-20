from pymongo import MongoClient
#常數區域#
DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS   = 'winners'
##########


nobel_winners = [
{'category': 'Physics',
'name': 'Albert Einstein',
'nationality': 'Swiss',
'sex': 'male',
'year': 1921},
{'category': 'Physics',
'name': 'Paul Dirac',
'nationality': 'British',
'sex': 'male',
'year': 1933},
{'category': 'Chemistry',
'name': 'Marie Curie',
'nationality': 'Polish',
'sex': 'female',
'year': 1911}
]

#誰是誰
client = MongoClient() 
#client = MongoClient('填位址') 
db     = client[DB_NOBEL_PRIZE]
coll   = db[COLL_WINNERS]

#資料進來
coll.insert(nobel_winners)

print(list(coll.find()))