#coding:MS950
#預設UTF-8,不是就加第一行那個

import example.hi as eh
#import as 叫package的example的py, as縮寫檔名,這個的內容會就印出來了喔
from sys import argv
# from import 叫package的sy的argv，要多打一個值來印
print('Hello',eh.name,'!')
print('argv:',argv[1])


