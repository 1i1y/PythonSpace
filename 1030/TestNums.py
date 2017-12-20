#欄位相加

import pandas as pd

df = pd.read_csv('nums.csv')

print(df.iloc[:,0])              #印第一列
print(df.iloc[:,1])              #印第二列
print(df.iloc[:,0]+df.iloc[:,1]) #第1+2列

df = pd.concat([df,df.iloc[:,0]+df.iloc[:,1]],axis=1) #axis=1 讓資料順利加在每筆數後方

print(df)