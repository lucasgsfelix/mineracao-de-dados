import numpy as np
from sklearn.svm import SVC
import pandas as pd

zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()

X =  zoo.drop(["name", "status"], axis = 1).values
y = zoo["status"]

neigh = gnb = GaussianNB()
neigh.fit(X, y) 

print clf.predict(X)
