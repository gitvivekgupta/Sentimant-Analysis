import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

lis = []

learndic = [0.2, 0.02, 0.002, 0.0002, 0.1, 0.01, 0.001, 0.0001]


icon = pd.read_csv('data4.csv')
X = icon[['pos_score', 'neu_score', 'neg_score', 'sub_score']]
y = icon['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

for learn in learndic:
        for depth in range(1, 10):
                for n in range(2, 200):
                        
                        clf = GradientBoostingClassifier(learning_rate=learn, max_depth=depth, n_estimators=n).fit(X_train, y_train)
                        score = clf.score(X_test, y_test)
                        lis.append(score)

                lis.sort()
                print(lis[-1], "||", depth, "||", learn)
                lis = []        

        print(".................")