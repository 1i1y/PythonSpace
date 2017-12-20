#list 清單 有順序，可重複值
#set  集合 沒順序，不重複值
#dict 字典

list = ['A','B','C','D']
set  = {'a','b','c','d'}

#使用join，不用擔心最後一項還加分隔符號
str1 = ','.join(list)
str2 = '|'.join(set)
print(str1)
#抓' '把句子拆成單字
str3  = 'My name is Nick'
list2 = str3.split(' ')
print(list2)