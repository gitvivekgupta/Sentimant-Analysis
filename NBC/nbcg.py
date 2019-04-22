import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


icon = pd.read_csv('data3.csv')

X = icon[['pos_score', 'neu_score', 'neg_score']]

y = icon['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = GaussianNB().fit(X_train, y_train)

score = clf.score(X_test, y_test)

print(score)