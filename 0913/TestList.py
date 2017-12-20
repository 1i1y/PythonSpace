lists=[4,1,2,3]
print (lists)
print (lists[0])
print (lists[1])
print (lists[2])
print (lists[3])
lists.append(4)
print (lists)
del lists[4]
print (lists)
'''聽說這也是註解
 list 清單 有順序，可重複值
 set  集合 沒順序，不重複值
 dict 字典
'''

sets={4,2,1,3}
print(sets)
sets.add(4)
print(sets)
sets.remove(4)
print(sets)

dicts={'a':1.1,'b':1.21}
print(dicts)
print(dicts['b'])
dicts['c']=1.3
print(dicts)
del dicts['a']
print(dicts)

tuples=(10,20,30)
print(tuples)
a,b,c= tuples
print(a)
print(b)
print(c)

x= 10
y= 20
x,y=y,x
print('x=',x)
print('y=',y)

