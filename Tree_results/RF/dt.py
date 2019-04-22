import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


lis = []

icon = pd.read_csv('data4.csv')
X = icon[['pos_score', 'neu_score', 'neg_score', 'sub_score']]
y = icon['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

for feat in range(1,5):
        for n in range(2,200):
                
                clf = RandomForestClassifier(n_estimators=n, max_features=feat).fit(X_train, y_train)
                score = clf.score(X_test, y_test)
                lis.append(score)

        lis.sort()
        print(lis[-1])
        lis = []        
