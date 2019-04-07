import csv
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

icon = pd.read_csv('out.csv')
label = pd.read_csv('data.csv')

X = icon[['pos_score', 'neu_score', 'neg_score']]

y = label['value']


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

myList = list(range(1,800))
neighbors = myList

n = []
k_val = []

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
    k_val.append(k)
    n.append(score)

plt.plot(n)

plt.ylabel('Accuracy Score')

plt.show()

n, k_val = zip(*sorted(zip(n, k_val)))

print(n[-1], "||", k_val[-1])