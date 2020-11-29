#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. dataframe column 선택하기

# #### column 선택하기
#   - 기본적으로 [ ]는 column을 추출 
#   - 컬럼 인덱스일 경우 인덱스의 리스트 사용 가능
#     - 리스트를 전달할 경우 결과는 Dataframe
#     - 하나의 컬럼명을 전달할 경우 결과는 Series

# In[1]:


import pandas as pd


# In[3]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv',index_col='Survived')
train_data.head()


# #### 하나의 컬럼 선택하기

# In[5]:


train_data['Name']


# #### 복수의 컬럼 선택하기

# In[7]:


train_data[['Age','Name']]


# In[ ]:




