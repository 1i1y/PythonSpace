#記得放值在跑喔~(2個小數)
import decimal #跑精準度的
from decimal import Decimal #讓程式簡潔的
import sys

d1 = decimal.Decimal(sys.argv[1])
d2 = decimal.Decimal(sys.argv[2])

print(d1+d2)
print(d1-d2)
print(d1*d2)
print(d1/d2)

print(0.1)
print(0.1+0.1)
print(0.1+0.1+0.1)#0.3000...04

print(decimal.Decimal('0.1')==0.1)#false
print(format(0.1,'.17f'))#其實0.1不是0.1，是0.1000...01

print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1'))
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))#from decimal import Decimal

