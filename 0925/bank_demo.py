import bank

acc = bank.Account('ABC','1222-0001',1000)     #這裡用bank才知道來自哪裡
print(acc)                                     #之後就認識acc了

acc.deposit(100)
acc.withdraw(10)
print(acc)

#acc.__name =""                                #如果bank.py沒有@property, 就會黏上來的新屬性還能印出來，但不會覆蓋舊的
acc.balance = -10                               #測試setter.balance 的規則能否正常 運作
print('戶名：',acc.name)
print('帳號：',acc.number)
print('餘額：',acc.balance)

acc1 = bank.Account.default('DEF','1222-0002')
print('戶名：', acc1.name)
print('帳號：', acc1.number)
print('餘額：', acc1.balance)