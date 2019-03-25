import csv
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier


icon = pd.read_csv('data.csv')

X = icon[['pos_score', 'neu_score', 'neg_score']]
y = icon['value']

myList = list(range(1,800))
neighbors = myList

cv_scores = []


for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())


MSE = [1 - x for x in cv_scores]

optimal_k = neighbors[MSE.index(min(MSE))]
print("The optimal number of neighbors is %d" % optimal_k)

plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()

cv_scores, neighbors = zip(*sorted(zip(cv_scores, neighbors)))
print(cv_scores[-len(cv_scores)], "||", neighbors[-len(neighbors)])
