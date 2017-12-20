#pandas~~
#檢查json的正確性 : https://jsonlint.com/


#欄列
import pandas as pd
df = pd.read_json('nobel_winners.json')
#print (df.columns)                #columns 索引 欄
#print (df.index)                  #index   索引 列

#取值的方法 : iloc = ix 功能
df = df.set_index('name')
#print (df.loc['Albert Einstein']) #是小括號，名字是'Albert Einstein'的
#print(df.head())                  #前5筆資料
#print (df.iloc[2])                #第3筆資料
#print (df.ix[2])                  #同上

#group
df = df.groupby('category')        #取category的做群組
#print(df.groups.keys())           #category的key

phy_group = df.get_group('Physics')#category群組的Physics
#print(phy_group.head())           #預設取前5筆

#範圍[:,:]
#print(phy_group.columns)          #columns 索引 欄
#print(phy_group.iloc[1])          #第2筆資料
#print(phy_group.iloc[1:4])
#print(phy_group.iloc[:,7])        #看第8列  
#print(phy_group.iloc[1:4,0:4])    #看第2~4行，第1~4列