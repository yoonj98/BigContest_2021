# -*- coding: utf-8 -*-
"""EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1knFoUtMU3XqhwvlS6-CcsB88pJ9Cf8EU
"""

# # 한글 폰트
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import matplotlib.pyplot as plt
import os
plt.rc('font', family='NanumBarunGothic') 
# %matplotlib inline

def func(df):
    d = {}
    d['use_amt_mean'] = df['use_amt'].mean()
    d['use_cnt_mean'] = df['use_cnt'].mean()

    return pd.Series(d, index=['use_amt_mean', 'use_cnt_mean'])
	

if __name__ == "__main__":
  ## 유동인구 데이터
  korean = pd.read_csv(os.path.join('..','raw', '제공데이터', '02-1_내국인유동인구_KOREAN.CSV'), encoding='CP949')
  korean_city = korean.groupby(['time','city'])['resd_pop_cnt','work_pop_cnt','visit_pop_cnt'].mean()
  korean_city = pd.DataFrame(korean_city)
  korean_city.reset_index(inplace=True)

  plt.figure()
  fig, ax = plt.subplots(2, 1, figsize = (11, 4))
  plt.rc('font', family='NanumBarunGothic') 

  sns.lineplot('time', 'resd_pop_cnt', data = korean_city, hue = 'city', palette="husl", alpha=.8, linewidth=3, ax=ax[0])
  ax[0].set(title='시간별 거주인구', ylabel = '인구수 ', xlabel='시간')

  sns.lineplot('time', 'work_pop_cnt', data = korean_city, hue = 'city', palette="husl", alpha=.8, linewidth=3, ax=ax[1])
  ax[1].set(title='시간별 근무인구', ylabel = '인구수 ', xlabel='시간')

  fig.tight_layout()
  plt.legend(loc = 'upper right')
  plt.show()

  del korean_city

  ## 카드소비 데이터
  card_spending = pd.read_csv(os.path.join('..','raw', '제공데이터', '04_음식관련 카드소비_CARD_SPENDING.CSV'), encoding='CP949')

  import datetime as dt

  card_spending['base_date'] = pd.to_datetime(card_spending['base_date'])
  card_spending['year'] = card_spending['base_date'].dt.year
  card_spending['month'] = card_spending['base_date'].dt.month
  card_spending['day'] = card_spending['base_date'].dt.day
  card_spending['week'] = card_spending['base_date'].dt.week
  card_spending['day_of_week'] = card_spending['base_date'].dt.weekday # 월요일 = 0

  card_spending_city = card_spending.groupby(['base_date', 'city']).apply(func)
  card_spending_city.reset_index(inplace=True)

  plt.figure()
  fig= plt.subplots(figsize = (15, 3))
  plt.rc('font', family='NanumBarunGothic') 

  p = sns.lineplot('base_date', 'use_amt_mean', data = card_spending_city, hue = 'city', palette="husl", alpha=.8, linewidth=3)
  plt.title('도시 및 일별 결제 금액')
  plt.xlabel('날짜')
  plt.ylabel('금액')
  plt.show()
