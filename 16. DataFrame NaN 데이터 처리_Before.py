#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. NaN 처리 방법 이해하기
# 

# In[3]:


import pandas as pd


# In[4]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv')
train_data.head()


# #### NaN 값 확인
#  - info함수를 통하여 개수 확인
#  - isna함수를 통해 boolean 타입으로 확인

# In[5]:


train_data.info()


# In[6]:


train_data.isna()


# In[7]:


train_data['Age'].isna()


# #### NaN 처리 방법
#  - 데이터에서 삭제
#    - dropna 함수 
#  - 다른 값으로 치환
#    - fillna 함수

# * NaN 데이터 삭제하기

# In[8]:


train_data.dropna()


# * NaN 값 대체하기
#  - 평균으로 대체하기
#  - 생존자/사망자 별 평균으로 대체하기

# In[9]:


train_data.dropna(subset=['Age'])


# In[10]:


train_data.dropna(axis=1)


# In[11]:


train_data['Age'].mean()


# In[12]:


train_data['Age'].fillna(train_data['Age'].mean())


# In[25]:


#생존자 나이 평균
mean1=train_data[train_data['Survived']==1]['Age'].mean()


# In[26]:


mean1


# In[27]:


#사망자 나이 평균
mean0=train_data[train_data['Survived']==0]['Age'].mean()


# In[28]:


mean1


# In[33]:


train_data[train_data['Survived']==1]['Age'].fillna(mean1)
train_data[train_data['Survived']==0]['Age'].fillna(mean0)


# In[35]:


train_data.loc[train_data['Survived']==1,'Age']= train_data[train_data['Survived']==1]['Age'].fillna(mean1)
train_data.loc[train_data['Survived']==0,'Age']= train_data[train_data['Survived']==0]['Age'].fillna(mean0)


# In[39]:


train_data[train_data['Age'] ==28.343689655172415]


# In[ ]:




