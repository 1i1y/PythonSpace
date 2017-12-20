
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_json('nobel_winners.json')
#df.info()  #看 Data columns 的項目的數量，檢查遺失的欄位
#df.columns #看 columns 的 欄名


# In[5]:


#df.describe() #看 欄的統計摘要


# In[6]:


#df.describe(include=['object']) #看欄的統計摘要，include針對要評估的欄的資料型別


# In[7]:


#df = df.set_index('name')
#df.head()


# In[8]:


#df.born_in.describe() #看 born_in 的統計摘要


# In[9]:


#set(df.born_in.apply(type)) #born_in 是 str 的形式


# In[10]:


#處理混雜類別
import numpy as np 
df.born_in.replace('',np.nan,inplace=True) #將空的轉成 NAN (NAN欄位不會被計算) ，已刪 born_in 一定有 error
df.born_in


# In[11]:


#df.born_in.describe() #真實數量降成 142


# In[12]:


#df.name = df.name.str.replace('*','') #先轉 str , 消 *
#df.name = df.name.str.strip()         #先轉 str , strip 消前後空白
#df.name


# In[13]:


#np.nan == np.nan >>> 會等於 false


# In[14]:


df = df[df.born_in.isnull()]        # isnull 看 born_in 值= NAN 的資料 ，如果開不起來 空 變 NAN 要打開
#df = df.drop('born_in', axis=1)     #刪 born_in 那欄
df.head()


# In[15]:


dupes_by_name = df[df.duplicated('name')]
dupes_by_name.count()
all_dupes = df[df.duplicated('name') | df.duplicated('name',keep='last')] 
#keep保留重複元素 : 最後一個last / 全刪'False / first , ∵ 重覆便不再重覆取值 ∴再加「  | df.duplicated('name',keep='last') 」
all_dupes.count()

for name, rows in df.groupby('name'):                       # for 迴圈找同名的有幾行(重覆得獎)
    print('name: %s, number of rows: %d'%(name, len(rows))) # %s 格式符 :字符串  %d 格式符 :一个整數。

pd.concat([g for _,g in df.groupby('name') if len(g) >1])   #列出重覆得獎


# In[16]:


df[df.gender.isnull()]['name']  #
df = df[df.gender.notnull()]
df.count()


# In[17]:


#import pandas as pd
#import numpy as np
#df = pd.read_json('nobel_winners.json')

####born_in clean####
df.born_in.replace('',np.nan,inplace=True)
df.born_in
df.born_in.describe()
####name clean####
df.name = df.name.str.replace('*','')
df.name = df.name.str.strip()
df.name
df = df[df.born_in.isnull()]
df = df.drop('born_in', axis=1)
df.head()
pd.concat([g for _,g in df.groupby('name') if len(g) >1])['name']
df = df[df.gender.notnull()]
df.count()

