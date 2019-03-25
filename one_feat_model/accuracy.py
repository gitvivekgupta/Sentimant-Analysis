import csv
import json
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

icon = pd.read_csv('data.csv')

X = icon[['score']]
y = icon['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

myList = list(range(1,800))
neighbors = myList

n = []

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
    n.append(score)

plt.plot(n)

plt.ylabel('Accuracy Score')

plt.show()
