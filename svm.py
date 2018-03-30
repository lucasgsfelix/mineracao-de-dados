import numpy as np
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import cross_val_score

zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()

X =  zoo.drop(["name", "status"], axis = 1).values
y = zoo["status"]

clf = SVC()
clf.fit(X, y)

scores = cross_val_score(clf, X, y, scoring = "f1_macro", cv=10)
print scores.mean()