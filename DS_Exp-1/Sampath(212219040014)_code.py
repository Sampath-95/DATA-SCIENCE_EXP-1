#!/usr/bin/env python
# coding: utf-8

# In[68]:


#B Sampath Kumar Rao - 212219040014
import pandas as pd


# In[69]:


df = pd.read_csv("C:\\Users\\banga\\gitremoterepo\\Ex-01_DS_Data_Cleansing\\Data_set.csv")


# In[70]:


df


# In[71]:


df.isnull().sum()


# In[72]:


df['show_name']=df['show_name'].fillna(df['show_name'].mode()[0])


# In[73]:


df


# In[74]:


df.isnull().sum()


# In[75]:


df.describe()


# In[76]:


df['aired_on']=df['aired_on'].fillna(df['aired_on'].mode()[0])


# In[77]:


df.isnull().sum()


# In[78]:


df['original_network']=df['original_network'].fillna(df['original_network'].mode()[0])


# In[79]:


df.isnull().sum()


# In[80]:


df['rating']=df['rating'].fillna(df['rating'].mode()[0])


# In[81]:


df.isnull().sum()


# In[82]:


df['current_overall_rank']=df['current_overall_rank'].fillna(df['current_overall_rank'].mode()[0])


# In[83]:


df.isnull().sum()


# In[84]:


df['rating']=df['rating'].fillna(df['rating'].mode()[0])


# In[85]:


df.isnull().sum()


# In[86]:


df['watchers']=df['watchers'].fillna(df['watchers'].mode()[0])


# In[87]:


df.isnull().sum()


# In[88]:


df

