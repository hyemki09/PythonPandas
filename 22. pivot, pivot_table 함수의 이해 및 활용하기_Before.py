#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. pivot, pivot_table 함수의 이해

# In[5]:


import numpy as np
import pandas as pd


# In[16]:


df = pd.DataFrame({
    '지역': ['서울', '서울', '서울', '경기', '경기', '부산', '서울', '서울', '부산', '경기', '경기', '경기'],
    '요일': ['월요일','월요일', '수요일', '월요일', '화요일', '월요일', '목요일', '금요일', '화요일', '수요일', '목요일', '금요일'],
    '강수량': [100, 80, 1000, 200, 200, 100, 50, 100, 200, 100, 50, 100],
    '강수확률': [80, 70, 90, 10, 20, 30, 50, 90, 20, 80, 50, 10]
                  })

df


# #### pivot 
#  - dataframe의 형태를 변경
#  - 인덱스, 컬럼, 데이터로 사용할 컬럼을 명시

# In[15]:


df.pivot('요일', '지역','강수량')


# #### pivot_table
#  - 기능적으로 pivot과 동일
#  - pivot과의 차이점
#    - 중복되는 모호한 값이 있을 경우, aggregation 함수 사용하여 값을 채움

# In[19]:


pd.pivot_table(df, index='요일',columns='지역', aggfunc=np.mean)


# In[ ]:




