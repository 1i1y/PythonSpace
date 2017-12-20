print(2*3)
print(2**3)
print(2**-3)
print(2^3)#??

print(10/3)
print(10//3)
print(10/3.0)
print(10//3.0)

a=3
b=7
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)
#字串也行
c='ABC'
d='DEF'
print(c>d)
print(c>=d)
print(c<d)
print(c<=d)
print(c==d)
print(c!=d)

print(3&7) #0011 &0111 ->0011 ->3
print(3|7) #0011 |0111 ->0111 ->7
print(3^7) #0011 ^0111 ->0100 ->4
print(~3)  #-4
print(bin(~3)) #-0b100
print(1<<2)#0001->0100->4
print(8>>3)#1000->0001->1

admin ={'A','B'}
users ={'A','c','d','e'}
print(admin &  users) #{'A'}
print(users -  admin) #{'e','d','c'}
print(admin ^  users) #{'e','d','c','B'}
print(admin >  users) #admin包括users，false
print(admin <  users) #users包括admin，false

nums =['A','B','C','D','E','F']
#      [0] [1] [2] [3] [4] [5]
nums1=nums
print(nums[0:3])  #['A','B','C'], 從0開始，到3前的list
print(nums[:2])   #['A','B'], 從0開始，到2前的list
print(nums[2:])   #['C','D','E','F'], 從2開始之後的list
print(nums[:-1])  #['A','B','C','D','E'], 從最後開始之前少一個的list
print(nums[0:4])  #['A','B','C','D']
print(nums[0:5:2])#['A','C','E']
print(nums[::2])  #['A','C','E']
print(nums[1:4])  #['B','C','D']
nums[1:4]=['b','c','d']
print(nums)       #['A','b','c','d','E','F']
print(nums1)      #['A','b','c','d','E','F']
del(nums[1:4]) 
print(nums1)      #['A','E','F']
