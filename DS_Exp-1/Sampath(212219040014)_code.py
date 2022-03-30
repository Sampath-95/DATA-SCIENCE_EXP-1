#!/usr/bin/env python
# coding: utf-8

# In[93]:


#B Sampath Kumar Rao - 212219040014
import pandas as pd


# In[94]:


df = pd.read_csv("C:\\Users\\banga\\gitremoterepo\\Ex-01_DS_Data_Cleansing\\Data_set.csv")


# In[95]:


df


# In[96]:


df.isnull().sum()


# In[97]:


df['show_name']=df['show_name'].fillna(df['show_name'].mode()[0])


# In[98]:


df


# In[99]:


df.isnull().sum()


# In[100]:


df.describe()


# In[101]:


df['aired_on']=df['aired_on'].fillna(df['aired_on'].mode()[0])


# In[102]:


df.isnull().sum()


# In[103]:


df['original_network']=df['original_network'].fillna(df['original_network'].mode()[0])


# In[104]:


df.isnull().sum()


# In[105]:


df['rating']=df['rating'].fillna(df['rating'].mean())


# In[106]:


df.isnull().sum()


# In[107]:


df['current_overall_rank']=df['current_overall_rank'].fillna(df['current_overall_rank'].median())


# In[108]:


df.isnull().sum()


# In[109]:


df['rating']=df['rating'].fillna(df['rating'].mode()[0])


# In[110]:


df.isnull().sum()


# In[111]:


df['watchers']=df['watchers'].fillna(df['watchers'].median())


# In[112]:


df.isnull().sum()


# In[113]:


df

