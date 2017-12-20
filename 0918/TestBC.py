#break continue
#沒有label, 只能用return
for i in range (0,10,1):
    if i==7:
        #break
        continue
    print(i)
   
score = int(input('請輸入成績:'))

if score >= 60:
    print('pass!!')
else:
    pass # 一個維持結構，但無用的fuction
    print('after if pass!!')

print('after pass!!')