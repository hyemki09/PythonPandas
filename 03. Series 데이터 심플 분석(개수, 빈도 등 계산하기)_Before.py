#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. Series 함수 활용하여 데이터 분석하기

# In[1]:


import numpy as np
import pandas as pd


# #### **Series size, shape, unique, count, value_counts 함수**
#  - size : 개수 반환
#  - shape : 튜플형태로 shape반환
#  - unique: 유일한 값만 ndarray로 반환
#  - count : NaN을 제외한 개수를 반환
#  - mean: NaN을 제외한 평균 
#  - value_counts: NaN을 제외하고 각 값들의 빈도를 반환 

# In[6]:


s = pd.Series([1,1,2,1,2,2,2,1,1,3,3,4,5,5,7,np.NaN])
s


# In[7]:


len(s)


# In[9]:


s.size


# In[10]:


s.shape


# In[11]:


s.unique()


# In[12]:


s.count()


# In[14]:


a= np.array([2,2,2,2,np.NaN])
a.mean()

b= pd.Series(a)
b.mean()


# In[15]:


s.mean()


# In[16]:


s.value_counts()


# In[18]:


s[[5,6,7]].value_counts()


# #### **head, tail 함수**
#  - head : 상위 n개 출력 기본 5개
#  - tail : 하위 n개 출력 기본 5개

# In[19]:


s.head()


# In[20]:


s.tail()


# In[ ]:





# In[ ]:





# In[ ]:




