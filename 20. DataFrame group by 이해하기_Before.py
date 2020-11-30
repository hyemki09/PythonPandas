#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. DataFrame groupby 이해하기

# In[1]:


import pandas as pd
import numpy as np


# #### group by
#   + 아래의 세 단계를 적용하여 데이터를 그룹화(groupping) (SQL의 group by 와 개념적으로는 동일, 사용법은 유사)
#     - 데이터 분할
#     - operation 적용
#     - 데이터 병합

# In[3]:


# data 출처: https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
df = pd.read_csv('../data/train.csv')
df.head()


# In[ ]:





# #### GroupBy groups 속성
#  - 각 그룹과 그룹에 속한 index를 dict 형태로 표현

# In[9]:


class_group=df.groupby('Pclass')
class_group


# In[10]:


class_group.groups


# In[12]:


gender_group = df.groupby('Sex')
gender_group.groups


# In[13]:


class_group.count()


# In[17]:


class_group.mean()


# In[23]:


df.groupby('Sex').mean()['Survived']


# #### groupping 함수
#  - 그룹 데이터에 적용 가능한 통계 함수(NaN은 제외하여 연산)
#  - count - 데이터 개수 
#  - sum   - 데이터의 합
#  - mean, std, var - 평균, 표준편차, 분산
#  - min, max - 최소, 최대값

# In[25]:





# #### 복수 columns로 groupping 하기
#  - groupby에 column 리스트를 전달
#  - 통계함수를 적용한 결과는 multiindex를 갖는 dataframe

# * 클래스와 성별에 따른 생존률 구해보기

# In[30]:


df.groupby(['Pclass','Sex']).mean()['Survived']


# In[28]:


df.groupby(['Pclass','Sex']).mean().index


# #### index를 이용한 group by
#  - index가 있는 경우, groupby 함수에 level 사용 가능
#    - level은 index의 depth를 의미하며, 가장 왼쪽부터 0부터 증가

# * **set_index** 함수
#  - column 데이터를 index 레벨로 변경
# * **reset_index** 함수
#  - 인덱스 초기화

# In[32]:


df.head()


# In[33]:


df.set_index(['Pclass','Sex'])


# In[34]:


df.set_index('Age').groupby(level=0).mean()


# In[36]:


import math
def age_categorize(age):
    if math.isnan(age):
        return -1
    return math.floor(age/10)*10


# In[41]:


df.set_index('Age').groupby(age_categorize).mean()['Survived']


# In[37]:


df.set_index('Age')


# #### MultiIndex를 이용한 groupping

# In[43]:


df.set_index(['Pclass','Sex']).groupby(level=[0,1]).mean()


# #### aggregate(집계) 함수 사용하기
#  - groupby 결과에 집계함수를 적용하여 그룹별 데이터 확인 가능

# In[45]:


df.set_index(['Pclass','Sex']).groupby(level=[0,1]).aggregate([np.mean,np.sum,np.max])


# In[ ]:




