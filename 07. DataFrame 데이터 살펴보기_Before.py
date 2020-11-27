#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. Dataframe data 살펴보기

# #### DataFrame
#   - Series가 1차원이라면 DataFrame은 2차원으로 확대된 버젼
#   - Excel spreadsheet이라고 생각하면 이해하기 쉬움
#   - 2차원이기 때문에 인덱스가 row, column로 구성됨
#    - row는 각 개별 데이터를, column은 개별 속성을 의미
#   - Data Analysis, Machine Learning에서 data 변형을 위해 가장 많이 사용

# In[1]:


import pandas as pd


# In[4]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/BIT-R45/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)\data/train.CSV')


# In[5]:


train_data


# #### head, tail 함수
#  - 데이터 전체가 아닌, 일부(처음부터, 혹은 마지막부터)를 간단히 보기 위한 함수

# In[6]:


train_data.head()


# In[7]:


train_data.tail()


# #### dataframe 데이터 파악하기
#  - shape 속성 (row, column)
#  - describe 함수 - 숫자형 데이터의 통계치 계산
#  - info 함수 - 데이터 타입, 각 아이템의 개수 등 출력

# In[8]:


train_data.shape


# In[10]:


train_data.describe()


# In[11]:


train_data.info()


# In[ ]:




