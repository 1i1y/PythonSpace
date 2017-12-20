#json 與 dict 檔 相似， "" 與 ''

import json

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

#方法1 dump
with open('nobel_winner.json','w') as f:
    json.dump(nobel_winners,f)
print(nobel_winners)
print('\n')

#方法2 load
with open('nobel_winner.json') as f:
    nobel_winners = json.load(f)
print(nobel_winners)   
