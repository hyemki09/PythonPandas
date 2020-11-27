#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. pandas Series 이해하기

# In[1]:


import numpy as np
import pandas as pd


# #### **Series 값 변경**
#   - 추가 및 업데이트: 인덱스를 이용
#   - 삭제: drop함수 이용
# 

# In[2]:


s = pd.Series(np.arange(100,105),['a','b','c','d','e'])


# In[5]:


s['a'] =200
s


# In[7]:


s['k'] = 300
s


# In[8]:


s.drop('k')


# In[10]:


s.drop('k',inplace=True)


# In[11]:


s


# In[13]:


s[['a','b']] =[300,900]
s


# #### **Slicing**
#  - 리스트, ndarray와 동일하게 적용

# In[15]:


s1 = pd.Series(np.arange(100,105))
s1


# In[16]:


s1[:3]


# In[18]:


s1[1:3]


# In[19]:


s2 =pd.Series(np.arange(100,105),['a','b','c','d','e'])


# In[20]:


s2[1:3]


# In[23]:


s2['c':'e']


# In[ ]:




