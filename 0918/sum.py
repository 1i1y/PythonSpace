def sum(*n):
    total =0
    for i in n:
        total+=i
    return total
def account(AID,PWD):
    return{'AID':AID,'PWD':PWD} #前後一致，才抓得到
    
    
print(sum(10,20))
print(sum(10,20,30))
print(sum(10,20,30,40))

params = {'AID':'Nick','PWD':'P@ssW0rd'}
print(account(**params))# "**params" 帳戶的params整個印出來