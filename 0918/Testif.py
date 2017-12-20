import sys

name = 'Guest'
if len(sys.argv)>1:
    name = sys.argv[1]
    print('Hello ',name, '有給名字下面不要理它')
print('Hello,',name,'同學你沒給我名字啊')