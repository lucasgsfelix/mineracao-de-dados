import numpy as np
from sklearn.naive_bayes import GaussianNB
import pandas as pd

zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()

X =  zoo.drop(["name", "status"], axis = 1).values
y = zoo["status"]

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y) 

print clf.predict(X)
