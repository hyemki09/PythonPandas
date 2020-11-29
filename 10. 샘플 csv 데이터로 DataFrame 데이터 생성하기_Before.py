#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. 수치해석 라이브러리인 numpy의 이해 및 사용
#  2. 데이터 분석 라이브러이인 pandas의 이해 및 사용

# #### csv 데이터로 부터 Dataframe 생성
#  - 데이터 분석을 위해, dataframe을 생성하는 가장 일반적인 방법
#  - 데이터 소스로부터 추출된 csv(comma separated values) 파일로부터 생성
#  - pandas.read_csv 함수 사용

# In[2]:


import pandas as pd


# In[3]:



# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv')
train_data.head()


# #### read_csv 함수 파라미터
#  - sep - 각 데이터 값을 구별하기 위한 구분자(separator) 설정 
#  - header - header를 무시할 경우, None 설정
#  - index_col - index로 사용할 column 설정
#  - usecols - 실제로 dataframe에 로딩할 columns만 설정

# In[9]:


train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv',index_col='Survived')


# In[10]:


train_data


# In[15]:


train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv',usecols=['Survived','Sex'])
train_data


# In[ ]:




