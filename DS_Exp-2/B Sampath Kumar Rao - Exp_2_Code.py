#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("C:\\Users\\banga\\gitremoterepo\\Ex-02_DS_Outlier\\weight.csv")


# In[4]:


df


# In[5]:


df.drop("Gender",axis=1,inplace=True)


# In[6]:


df


# In[7]:


# df=df.drop("Gender",axis=1,inplace=True)


# In[8]:


df.boxplot()


# In[9]:


from scipy import stats


# In[10]:


import numpy as np


# In[11]:


z=np.abs(stats.zscore(df))


# In[12]:


z


# In[13]:


df


# In[14]:


df1=df.copy()


# In[15]:


df1=df1[(z<3).all(axis=1)]


# In[16]:


df1.boxplot()


# In[17]:


df1


# In[18]:


#interquartile method
df2=df.copy()


# In[19]:


q1=df2.quantile(0.25)


# In[20]:


q3=df2.quantile(0.75)


# In[21]:


IQR=q3-q1
IQR


# In[22]:


IQR.Height


# In[23]:


df2_new=df2[((df2>=q1-1.5*IQR)&(df2<=q3+1.5*IQR)).all(axis=1)]


# In[24]:


df2


# In[ ]:




