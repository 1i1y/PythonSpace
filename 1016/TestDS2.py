import dataset
db = dataset.connect('sqlite:///nobel_prize.db')
#刪叫winner的db, 
wtable=db['winners']
wtable.drop()
#刪了之後這邊就不影響了
wtable = db['winners']
winners = wtable.find()
winners = list(winners)

print(winners)