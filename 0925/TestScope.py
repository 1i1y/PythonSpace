# 模組           global
#   函式         nonlocal
#     子函式

x = 10 #模組變數

def fun():
    #global x #強迫成為模組變數
    x = 20    #函式變數
    print(x)
    
fun()
print(x)      #global->20, 沒有的話 ->10

