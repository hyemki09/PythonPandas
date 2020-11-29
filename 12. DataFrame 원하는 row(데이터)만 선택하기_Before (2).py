#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. dataframe row 선택하기

# In[10]:


import pandas as pd
import numpy as np


# In[11]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv')
train_data.head()


# #### dataframe slicing
#   - dataframe의 경우 기본적으로 [] 연산자가 **column 선택**에 사용
#   - 하지만, slicing은 row 레벨로 지원

# In[12]:


train_data[:10]


# #### row 선택하기
#   - Seires의 경우 []로 row 선택이 가능하나, **DataFrame의 경우는 기본적으로 column을 선택하도록 설계**
#   - **.loc, .iloc함수**로 row 선택 가능
#     - loc - 인덱스 자체를 사용
#     - iloc - 0 based index로 사용
#     - 이 두 함수는 ,를 사용하여 column 선택도 가능

# In[13]:


train_data.info()


# In[14]:


train_data.index = np.arange(100,991)


# In[15]:


train_data.tail()


# In[16]:


train_data.loc[986]


# In[17]:


train_data.loc[[100,920,930]]


# In[18]:


train_data.iloc[0]


# In[19]:


train_data.loc[[986,930,910],['Survived','Name','Age']]


# In[24]:


train_data.iloc[[100,101,103], [1,4,5]]


# In[ ]:




