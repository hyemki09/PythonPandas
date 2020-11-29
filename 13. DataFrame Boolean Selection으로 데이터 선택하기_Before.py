#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. Dataframe boolean selection 이해하기

# In[1]:


import pandas as pd


# In[2]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv')
train_data.head()


# #### **boolean selection으로 row 선택하기**
#  - numpy에서와 동일한 방식으로 해당 조건에 맞는 row만 선택

# #### 30대이면서 1등석에 탄 사람 선택하기 

# In[8]:


Class = train_data['Pclass']==1
Age = (train_data['Age']>=30) & (train_data['Age']<40)

Age


# In[11]:


train_data[Class & Age]


# In[ ]:




