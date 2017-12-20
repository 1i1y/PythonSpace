#附加新資料 : Series concat

import pandas as pd

df = pd.read_csv('data.csv', names=['name','category'], skipinitialspace=True)  # skipinitialspace 跳過空白跟分隔符號

s  = pd.Series([1911,1952])   #附加的新資料
df = pd.concat([df,s],axis=1) #axis=1 讓資料順利加在每筆數後方, concat 資料掛上去

print(df)