#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. Series boolean selection 활용하기

# In[1]:


import numpy as np
import pandas as pd


#  #### **Boolean selection**
#   - boolean Series가 []와 함께 사용되면 True 값에 해당하는 값만 새로 반환되는 Series객체에 포함됨
#   - 다중조건의 경우, &(and), |(or)를 사용하여 연결 가능

# In[3]:


s = pd.Series(np.arange(10), np.arange(10)+1)
s


# In[4]:


s > 5


# In[5]:


s[s>5]


# In[6]:


s % 2 == 0


# In[7]:


s[s%2 == 0]


# In[8]:


s. index >5


# In[9]:


s[s. index >5]


# In[13]:


(s.index>5)&(s<8)


# In[12]:


s[(s>5)&(s<8)]


# In[ ]:




