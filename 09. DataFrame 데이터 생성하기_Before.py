#!/usr/bin/env python
# coding: utf-8

# ## 학습목표
#  1. 수치해석 라이브러리인 numpy의 이해 및 사용
#  2. 데이터 분석 라이브러이인 pandas의 이해 및 사용

# #### DataFrame 생성하기
#  - 일반적으로 분석을 위한 데이터는 다른 데이터 소스(database, 외부 파일)을 통해 dataframe을 생성
#  - 여기서는 실습을 통해, dummy 데이터를 생성하는 방법을 다룰 예정

# In[ ]:


import pandas as pd


# #### dictionary로 부터 생성하기
#  - dict의 key -> column

# In[ ]:


data = {'a': 100, 'b': 200, 'c': 300}
pd.DataFrame(data, index = [0, 1, 2])


# In[ ]:


data = {'a' : [100, 200, 300], 'b': [1, 2, 3], 'c': [4, 5, 6]}
pd.DataFrame(data, index=[100, 200, 300])


# #### Series로 부터 생성하기
#  - 각 Series의 인덱스 -> column

# In[ ]:


a = pd.Series([100, 200, 300], ['a', 'b', 'c'])
b = pd.Series([101, 202, 303], ['a', 'b', 'c'])
c = pd.Series([110, 220, 330], ['a', 'b', 'c'])

pd.DataFrame([a, b, c])


# In[ ]:




