#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. 숫자 & 범주형 데이터의 이해

# In[2]:


import pandas as pd


# In[7]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('../data/train.csv')
train_data.head()


# #### info함수로 각 변수의 데이터 타입 확인
#  - 타입 변경은 astype함수를 사용

# In[8]:


train_data.info()


# In[11]:


train_data['Pcalss']=train_data['Pclass'].astype(str)


# In[13]:


import math


# In[15]:


def age_categorize(age):
    if math.isnan(age):
        return -1
    return math.floor(age / 10) * 10


# In[16]:


train_data['Age'].apply


# In[19]:


pd.get_dummies(train_data, columns=['Pclass','Sex','Embarked'])


# In[ ]:




