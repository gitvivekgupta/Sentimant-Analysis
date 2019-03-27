import csv
import pandas as pd
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df_new = df.loc[:,"pos_score":"sub_score"].div(100, axis=0).round(4)

df_new.to_csv('norm_100.csv', sep=',')
