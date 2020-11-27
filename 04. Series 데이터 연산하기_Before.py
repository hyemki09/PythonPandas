#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. Series 데이터 연산하기

# In[1]:


import numpy as np
import pandas as pd


# #### index를 기준으로 연산

# In[2]:


s1 = pd.Series([1,2,3,4],['a','b','c','d'])
s2 = pd.Series([6,3,2,1],['d','c','b','a'])
s1


# In[3]:


s2


# In[4]:


s1+s2


# #### **산술연산**
#  - Series의 경우에도 스칼라와의 연산은 각 원소별로 스칼라와의 연산이 적용
#  - Series와의 연산은 각 인덱스에 맞는 값끼리 연산이 적용
#    - 이때, 인덱스의 pair가 맞지 않으면, 결과는 NaN 

# In[5]:


s1 ** 2


# In[6]:


s1 ** s2


# #### **index pair가 맞지 않는 경우**
#  - 해당 index에 대해선 NaN 값 생성

# In[7]:


s1['k'] = 7
s2['e'] = 9
s1


# In[8]:


s2


# In[9]:


s1 + s2


# In[ ]:




