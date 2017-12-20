#讀csv檔

from io import StringIO  # io 是小寫!!!!!!!!!!!!!!!!!!!!!! 
import pandas as pd

df = pd.read_csv('data.csv', names=['name','category'], skipinitialspace=True) #skipinitialspace 跳過空白跟分隔符號
print(df)

df.to_csv('data_new.csv', encoding='utf-8')
data = "'Albert Einstein'|Physics \n 'Marie Curie'|Chemistry"
df = pd.read_csv(StringIO(data) , sep='|' , names=['name','category'],
    skipinitialspace=True, quotechar="'")
    
print(df)