﻿def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)

m = int(input('數字1:'))
n = int(input('數字2:'))

r = gcd(m,n)
if r==1:
    print('互質')
else:
    print('最大公因數:',r)
    

