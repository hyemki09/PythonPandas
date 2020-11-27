#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. pandas Series 데이터 생성하기

# In[1]:


import numpy as np
import pandas as pd


# #### Series
#   - pandas의 기본 객체 중 하나
#   - numpy의 ndarray를 기반으로 인덱싱을 기능을 추가하여 1차원 배열을 나타냄
#   - index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성, 지정할 경우 명시적으로 지정된 index를 사용
#   - 같은 타입의 0개 이상의 데이터를 가질 수 있음

# * data로만 생성하기
#  - index는 기본적으로 0부터 자동적으로 생성

# In[3]:


s1 = pd.Series([1,2,3])
s1


# In[4]:


s2 = pd.Series(['a','b','c'])
s2


# In[6]:


s3 = pd.Series(np.arange(200))
s3


# * data, index함께 명시하기

# In[8]:


s4 = pd.Series([1,2,3],[100,200,300])
s4


# In[9]:


s5 = pd.Series([1,2,3],['a','m','k'])
s5


# * data, index, data type 함께 명시하기

# In[17]:


s6 = pd.Series(np.arange(5),np.arange(100,105),dtype=np.int32)
s6


# #### 인덱스 활용하기

# In[18]:


s6.index


# In[19]:


s6.values


# 1. 인덱스를 통한 데이터 접근

# In[21]:


s6[100]


# In[22]:


s6[103]


# 2. 인덱스를 통한 데이터 업데이트

# In[26]:


s6[104] = 70
s6


# In[27]:


s6[105] = 90
s6[200] = 80
s6


# 3. 인덱스 재사용하기

# In[29]:


s7 = pd.Series(np.arange(7),s6.index)
s7


# In[ ]:




