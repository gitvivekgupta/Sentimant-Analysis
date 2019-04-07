import csv
import pandas as pd
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df_new = df.loc[:,"pos_score":"neg_score"].div(50, axis=0)

df_new.to_csv('out.csv', sep=',')