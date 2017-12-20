def xrange(n):
    x=0
    while x!=n :
        yield x             #禮讓->先印 for in ->yield ->for in ->yield ...
        print('Yield:',x)
        x+=1


print(type(xrange))         #型態:function
print(type(xrange(10)))     #型態:generator 產生器，生一個範圍的數值出來，一次一個

for n in xrange(10):
    print('For in:', n)
    

""" 解說
def xrange(n): # n=3
    x = 0
    while x!=n:# 0!=3  1!=3   2!=3   3!=3
        yield x# 禮讓0 禮讓1  禮讓2
        print('Yield:' , x) # 0 1 2
        x+=1   # x=1  x=2    x=3

print(type(xrange))
print(type(xrange(10)))
        
for n in xrange(3):# 0  1   2
    print('For in:', n ) # 0  1  2
"""