import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier



zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()
X =  zoo.drop(["name", "status"], axis = 1).values
y = zoo["status"]

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y) 

scores = cross_val_score(neigh, X, y, scoring = "f1_macro", cv=10)

print scores