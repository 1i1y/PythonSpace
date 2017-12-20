#課堂作業，判斷輸入是基偶數(V)
score1=int(input('請輸入英文成績:'))
score2=int(input('請輸入數學成績:'))

if score1 >=60: #if  else 後面是"分號" 
    if score2>=60:
        print('都及格，了不起喔~來戰啊!!!!!')
    else:
        print('我知道這次數學很難，拍拍~')

if score1 >=60:  
    if score2>=60:
        print('及格~及格~灑花~花~')
else:
    print('這世界英文不及格，什麼都不是~')        