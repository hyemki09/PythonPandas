#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. corr 함수 이용하기

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('C:/Users/Hyemyung/Downloads/[전체강의자료]머신러닝과-데이터분석-a-z/Part 01~04) Python/04. 데이터 분석을 위한 Python (Pandas)/data/train.csv')
train_data.head()


# #### 변수(column) 사이의 상관계수(correlation) 
#  - corr함수를 통해 상관계수 연산 (-1, 1 사이의 결과)
#    - 연속성(숫자형)데이터에 대해서만 연산
#    - 인과관계를 의미하진 않음

# In[4]:


train_data.corr()


# In[5]:


plt.matshow(train_data.corr())


# In[ ]:




