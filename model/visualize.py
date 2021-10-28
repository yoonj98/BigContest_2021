# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_C040NVPhhsxyDywkUXVx8epy8fIeaPR
"""

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import pandas as pd
import numpy as np
import os
from pycaret.regression import *
import shap

np.random.seed(777)

def make_plot_jeju(city_nm):
  for i in city_nm:
    s = setup(data = globals()['data_{}'.format(i)], train_size = 0.7, target = 'em_g', fold_strategy = 'timeseries', fold = 3,
                ignore_features = ['base_date', 'city', 'emd_nm'],silent = True, verbose = True, session_id = 777,
                remove_outliers = True)
    best = compare_models(include=['lightgbm','dt','rf','et'], sort = 'RMSE')
    print(best)
    globals()['model_{}'.format(i)] = create_model(best, cross_validation = False)
    globals()['model_{}_tuned'.format(i)] = tune_model(globals()['model_{}'.format(i)], optimize = 'RMSE', n_iter = 10)

    evaluate_model(globals()['model_{}_tuned'.format(i)])
    plot_model(globals()['model_{}_tuned'.format(i)])
    interpret_model(globals()['model_{}_tuned'.format(i)])
    interpret_model(globals()['model_{}_tuned'.format(i)], plot = 'reason', observation = 12)
    interpret_model(globals()['model_{}_tuned'.format(i)], plot='correlation')
    plot_model(globals()['model_{}_tuned'.format(i)], plot = 'feature')


if __name__ == "__main__":
  data = pd.read_csv(os.path.join('..','preprocess', 'total_data_final_known_end.csv'))
  data['7_people'] = data['7_people'].replace('X','0')
  data['7_people'] = data['7_people'].astype(float)
  data['apartment'] = data['apartment'].replace('X','0')
  data['apartment'] = data['apartment'].astype(float)
  data.drop('geo_type', axis =1, inplace = True)

  data_remov = data.drop(['em_cnt', 'pay_amt', 'em_g_per_cnt', 'em_cnt_variant', 'em_g_variant', 
                'pay_amt_variant', 'em_g_per_cnt_variant', 'observed', 'trend', 'seasonal'], axis=1)
  제주시 = data_remov[data_remov['city'] == '제주시'].emd_nm.unique()
  for i in 제주시:
    globals()['data_{}'.format(i)] = data_remov[data_remov.emd_nm == i]
  
  data_일도1동 = data_일도1동[data_일도1동['base_date']<="2021-06-13"]
  data_한림읍 = data_한림읍[data_한림읍['base_date']>="2019-11-12"]
  data_구좌읍 = data_구좌읍[data_구좌읍['base_date']>="2019-11-12"]
  data_한경면 = data_한경면[data_한경면['base_date']>="2019-11-12"]
  data_조천읍 = data_조천읍[data_조천읍['base_date']>="2019-11-12"]
  data_애월읍 = data_애월읍[data_애월읍['base_date']>="2019-11-12"]

  make_plot_jeju(제주시) 

  서귀포시 = data_remov[data_remov['city'] == '서귀포시'].emd_nm.unique()
  for i in 서귀포시:
    globals()['data_{}'.format(i)] = data_remov[data_remov.emd_nm == i]

  make_plot_jeju(서귀포시)
