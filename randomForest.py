import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score
#%matplotlib inline
zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X =  zoo.drop(["name", "status"], axis = 1).values
y = zoo["status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50)

rfc = RandomForestClassifier(n_estimators=50)
rfc.fit(X_train,y_train)


predict = rfc.predict(X_test)
print classification_report(y_test, predict)

scores = cross_val_score(rfc, X, y, scoring = "f1_macro", cv=10)
print scores.mean()