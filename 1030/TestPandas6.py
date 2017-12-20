#讀mongodb, 需先開 mongod.exe 
#cd C:\Program Files\MongoDB\Server\3.4\bin
#mongod.exe --dbpath C:\mongodb\data

import pandas as pd
from pymongo import MongoClient

client = MongoClient()
db     = client.nobel_prize
cursor = db.winners.find()
df     = pd.DataFrame(list(cursor))

print(df)
