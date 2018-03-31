#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from sklearn.feature_selection import VarianceThreshold
import pandas as pd

zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()

X =  zoo.drop(["name", "status"], axis = 1).values
y = zoo["status"]
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)
print sel