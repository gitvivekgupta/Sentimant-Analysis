import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


fig= plt.figure()

ax = fig.add_subplot(111, projection='3d')

depth = [100, 1000, 2000, 3000, 4000, 5000, 6000]

lis_x = []
lis_y = []
lis_z = []

icon = pd.read_csv('data7.csv')
X = icon[['pos_score', 'neu_score', 'neg_score', 'pos_sub_score', 'neu_sub_score', 'neg_sub_score',]]
y = icon['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

for n in depth:
        for g in range(1000,6000):
                clf = DecisionTreeClassifier(min_samples_split=g, max_depth=n, max_features=6).fit(X_train, y_train)
                score_ = clf.score(X_test, y_test)
                lis_x.append(score_)
                lis_y.append(g)
                lis_z.append(n)
                
        
ax.scatter(lis_x, lis_y, lis_z, c='b', marker='o')

ax.set_xlabel('score')
ax.set_ylabel('split')
ax.set_zlabel('depth')

plt.show()

lis_x.sort()
print(lis_x[-1])