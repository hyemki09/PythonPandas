#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. Dataframe에 새로운 colum을 추가하기
#  2. Dataframe에 column 삭제하기

# In[1]:


import pandas as pd


# In[14]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv')
train_data.head()


# #### 새 column 추가하기
#  - [] 사용하여 추가하기
#  - insert 함수 사용하여 원하는 위치에 추가하기

# In[16]:


train_data['Age_Double'] = train_data['Age'] * 2
train_data.head()


# In[23]:


train_data.insert(3,'Fare20',train_data['Fare']/10)
train_data.head()


# In[ ]:





# #### column 삭제하기
#  - drop 함수 사용하여 삭제
#    - 리스트를 사용하여 멀티플 삭제 가능 

# In[25]:


train_data.drop('Age_Double',axis=1)
train_data.head()


# In[26]:


train_data.drop('Age_Double',axis=1, inplace=True)


# In[27]:


train_data.head()


# In[ ]:




