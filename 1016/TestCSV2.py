import csv
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


with open('nobel_winner.csv','w',newline='\n') as f:
#版本3以上後只能是'w'，再加上新舊版本的差異轉換時會產生一堆空白，使用newline轉成'\n'
    fs = list(nobel_winners[0].keys())
    # fs 是 資料的key
    fs.sort()
    #排序
    writer = csv.DictWriter(f,fieldnames=fs)"
    #fieldnames 是 fs
    writer.writeheader()             #寫欄名
    for w in nobel_winners:          #寫值
        writer.writerow(w)

# [()]
with open('nobel_winner.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print(nobel_winners)

#dict結構，長這樣…[OrderedDict([])
with open('nobel_winner.csv') as f:
    reader = csv.DictReader(f)
    nobel_winners = list(reader)
print(nobel_winners)
f.close

