name='Justin'
print('Hello ', end=' ')
print(name)
print('Hello',name,name,sep=',')
print('{}除以{}是{}'.format(10,3,10/3))
print('{n1}除以{n2}是{result}'.format(n1=10,n2=3,result=10/3))

print('{n1:d}除以{n2:d}是{result:f}'.format(n1=10,n2=3,result=10/3))
print('{n1:5d}除以{n2:5d}是{result:10.2f}'.format(n1=10,n2=3,result=10/3))
print('{n1:<3d}除以{n2:<3d}是{result:.2f}'.format(n1=10,n2=3,result=10/3))
print('{n1:>3d}除以{n2:>3d}是{result:.2f}'.format(n1=10,n2=3,result=10/3))
print('{n1:<3d}除以{n2:<3d}是{result:.2f}'.format(n1=10,n2=3,result=10/3))
print('{n1:*^10d}除以{n2:!^10d}是{result:.10f}'.format(n1=10,n2=3,result=10/3))

names=['Nick','Monica','Justin']
print('All names:{n[0]},{n[1]},{n[2]}'.format(n=names))
passwords ={'AAA':112234,'BBB':223345}
'''key_value'''
print('你的密碼{p[AAA]},你朋友的密碼{p[BBB]}'.format(p=passwords))