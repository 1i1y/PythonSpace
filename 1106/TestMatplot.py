
# coding: utf-8

# In[58]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib

np.random.seed(9989) #seed隨機亂數子
x = pd.period_range(pd.datetime.now(),periods=200,freq='d') # d => day
x = x.to_timestamp().to_pydatetime() #timestamp 時間序列呈現
y = np.random.randn(200,3).cumsum(0) #值(個數，條) #cumsum 返回累加值
plots = plt.plot(x,y)


# In[59]:


plots = plt.plot(x,y,label='')
plt.gcf().set_size_inches(8,4)
plt.legend(plots,('foo','bar','baz'),loc='best',framealpha=0.25,prop={'size':'small','family':'monospace'})
plt.title('Random Trends')
plt.xlabel('Date')
plt.ylabel('Cum. sum')
plt.grid(True) #隔線
plt.figtext(0.995,0.01,'@ Lily Design 2017',ha='right',va='bottom')


# In[60]:


fig = plt.figure(figsize=(8,4))
# 主要軸
ax  = fig.add_axes([0.1,0.1,0.8,0.8]) #figure.add_axes 插入圖表
ax.set_title('Main Axes with Insert Child Axes')
ax.plot(x,y[:,0])
ax.set_xlabel('Date')
ax.set_ylabel('Cum. sum')
# 插入子軸
ax  = fig.add_axes([0.15,0.15,0.3,0.3]) #figure.add_axes 插入圖表
ax.plot(x,y[:,2],color='g')
ax.set_xticks([]);


# In[61]:


fig, axes = plt.subplots(nrows=3,ncols=1,sharex=True,sharey=True,figsize=(8,8))
labelled_data = zip(y.transpose(),('foo','bar','baz'),('b','g','r'))
fig.suptitle('Three  Random Trends',fontsize = 16)

for i,ld in enumerate(labelled_data):
    ax = axes[i]
    ax.plot(x,ld[0],label=ld[1],color=ld[2])
    ax.set_ylabel('Cum. sum')
    ax.legend(loc='upper left',framealpha=0.5,prop={'size':'small'})
axes[-1].set_xlabel('Date')


# In[69]:


labels = ['Physics','Chemistry','Literature','Peace']
data   = [3,6,10,4]

bar_width=0.5
xlocations = np.array(range(len(data)))+bar_width

plt.bar(xlocations, data, width=bar_width)
plt.yticks(range(0,12))
plt.xticks(xlocations+bar_width/2,labels)
plt.xlim(0,xlocations[-1]+bar_width*2)
plt.title('Prizes won by Fooland')

plt.gca().get_xaxis().tick_bottom()
plt.gca().get_yaxis().tick_left()
plt.gcf().set_size_inches((8,4))


# In[75]:


np.random.seed(9989)
num_points = 100
gradient   = 0.5
x = np.array(range(num_points))
y = np.random.randn(num_points)*10 + x*gradient
fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(x,y)

m, c = np.polyfit(x,y,1)
ax.plot(x,m*x+c)

fig.suptitle('A Simple Scatterplot')


# In[85]:


import seaborn as sns 
data= pd.DataFrame({'dummy x':x,'dummy y':y})
sns.lmplot('dummy x','dummy y',data,size=6,aspect=3)


# In[93]:


tips=sns.load_dataset('tips')
tips


# In[96]:


g= sns.FacetGrid(tips,col='smoker',size=6,aspect=1)
g.map(plt.scatter,'total_bill','tip')


# In[99]:


iris =sns.load_dataset('iris')
iris


# In[106]:


sns.set(font_scale=1.2)
g = sns.PairGrid(iris,hue="species",size=4,aspect=1)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)
g.add_legend()

