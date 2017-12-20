nums1 = {1,2,3} #set
nums2 = [1,2,3] #List
nums3 = (1,2,3) #Turple

#增加的方法
nums1.add(4)
nums2.append(4)

for n in nums1:
    print(n)
    
for i in range(len(nums2)):
    print ('nums2[',i,']=',nums2[i])