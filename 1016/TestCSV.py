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

cols = list(nobel_winners[0].keys()) 
#keys 叫出cols的所有欄位
cols.sort()

with open ('nobel_winner.csv','w') as f : 
# 'w' << 寫入
    f.write(','.join(cols)+'\n')
    #欄位名稱
    for o in nobel_winners:
        for col in cols:
            row = str(o[col])
        f.write(','.join(row)+'\n')
        #內容
                 
        #row = [ str(o[col]) for col in cols]
        #print(row) 看行的資料
        #f.write(','.join(row)+'\n')
        #print(o['category'],',',o['name'],',',o['nationality'],',',o['sex'],',',o['year']) 與上方效果相同
        #原本內容
       
with open('nobel_winner.csv') as f:
#寫出
    for line in f.readlines():
    #讀每一行，但會多出很多空白
        line = line.strip()
        #所以寫這行清空白
        print(line)
        
f.close
