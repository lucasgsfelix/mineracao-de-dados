### esse algoritmo sera responsavel por fazer cog-os que eh classification using local clustering

import pandas as pd
from sklearn.cluster import KMeans
from imblearn.over_sampling import SMOTE

def cogOs(data):

	X =  zoo.drop(["name", "status"], axis = 1).values
	y = zoo["status"]

	kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
	kmeans.cluster_centers_

	X_resampled, y_resampled = SMOTE().fit_sample(X, y)
	clf_smote = LinearSVC().fit(X_resampled, y_resampled)
	





zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()
cogOs(zoo)