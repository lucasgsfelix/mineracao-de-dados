import numpy as np
from sklearn.naive_bayes import GaussianNB
import pandas as pd

zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()

X =  zoo.drop(["name", "status"], axis = 1).values
y = zoo["status"]

gnb = GaussianNB()
gnb.fit(X, y) 

print gnb.predict(X)
