import csv
import pandas as pd
import numpy as np
from matplotlib import cm

df = pd.read_csv('data.csv')

df_new = df.loc[:,"pos_score":"neg_sub_score"].mul(100).astype(int).div(10000)

df_new.to_csv('norm_100.csv', sep=',')