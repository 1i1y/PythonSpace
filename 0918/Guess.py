import random

#謎底=i
i = random.randint(1,10)
useri = 0
times = 0
print(i,'<<這是答案，但請你假裝看不見，謝謝~')


#輸入謎底答案
# while
while useri != i:
    useri =int(input('請輸入數字:'))
    times +=1
    if(useri>i):
        print('第',times,'次,比謎底數字大：', useri)
    else:
        print('第',times,'次,比謎底數字小：', useri)
print('恭喜你猜對了：', useri,'同答案再猜一次')


# while True
Count = 0
while True:
    Count+=1
    print('第',Count,'次猜數字，', end='')
    useri = int(input('請輸入你要猜的數字：'))
    if useri > i :
        print('比謎底數字大：', useri)
    elif useri < i  :
        print('比謎底數字小：', useri)
    else:
        print('恭喜你猜對了：', useri)
        break;