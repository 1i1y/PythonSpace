# pickle 轉序列化 

import pickle
s = {'Nick','Alan'} # set 集合
pkd = pickle.dumps(s)

print (pkd)
print (pickle.loads(pkd))
