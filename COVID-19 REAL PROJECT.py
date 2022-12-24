#!/usr/bin/env python
# coding: utf-8

# # COVID-19 SMALL DATASET
# 

# In[1]:


import pandas as pd


# In[41]:


data =pd.read_csv(r"C:\Users\Rahul Dev Sharma\Downloads\4. covid_19_data.csv")


# In[6]:


data


# In[7]:


data.count()


# In[10]:


data.isnull().sum()


# In[11]:


import seaborn as sns


# In[12]:


import matplotlib.pyplot as plt


# In[13]:


sns.heatmap(data.isnull())
plt.show()


# Q.1) Show the number of Confirmed ,Deaths and Recovered cases in each Region

# In[14]:


data.head(2)


# In[18]:


data.groupby('Region').sum().head(20)


# In[24]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False)


# In[25]:


data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False).head(20)


# In[29]:


data.groupby('Region')['Deaths','Recovered'].sum()


# Q.2) Remove all records where Confiemed cases is less than 10

# In[30]:


data.head(2)


# In[36]:


data.Confirmed < 10


# In[37]:


data[data.Confirmed < 10] 


# In[38]:


data = data[~(data.Confirmed < 10)]


# In[39]:


data


# Q.3) In which Region,maximum number of Confirmed cases were recorded?

# In[42]:


data


# In[46]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(10)


# Q.4) In which region minimun number of death were recorded?

# In[50]:


data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50)


# Q.5) How many confirmed ,deaths and recovered cases were reported from India till April 2020?

# In[53]:


data[data.Region =='India']


# In[54]:


data[data.Region =='US']


# Q.6-A) Sort the entire data wrt No. of confirmed cases in ascending order.

# In[55]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = True)


# Q.6-A) Sort the entire data wrt No. of confirmed cases in ascending order.2nd way

# In[56]:


data.sort_values(by = ['Confirmed'], ascending = True)

#Q.6-B) Sort the entire data wrt No. of recovered cases in descending order.
# In[59]:


data.sort_values(by = ['Recovered'], ascending = False)


# In[ ]:




