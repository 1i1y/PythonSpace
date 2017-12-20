import dataset
db = dataset.connect('sqlite:///nobel_prize.db')
#創個db叫winner, find 找
wtable = db['winners'] 
winners = wtable.find()
winners = list(winners)

print(winners)