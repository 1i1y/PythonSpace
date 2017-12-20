#for迴圈的三種寫法
nums =[1,2,3,4,5,6]

for i in range(len(nums)):
    print (nums[i])
    #i 0->5

for i in nums:
    print (i)

for i in range(len(nums)):
    print('nums[{0}]={1}'.format(i,nums[i]))
    #i 0->5

for i in range(0,2,1): #從0開始到2，每1個的list
    print('nums[{0}]={1}'.format(i,nums[i]))
   
passwds ={'AAA':123,'BBB':456}   #什麼00123的00不行啊~會影響不能跑
for ID,Pass in passwds.items():
    print(ID,Pass)

