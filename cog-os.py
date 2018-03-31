### esse algoritmo sera responsavel por fazer cog-os que eh classification using local clustering

import pandas as pd
from sklearn.cluster import KMeans
from imblearn.over_sampling import SMOTE
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
def cogOs(data):

	X =  zoo.drop(["name", "status"], axis = 1).values
	y = zoo["status"]

	#wcss = []
	#for i in range(1, 11):
	#	kmeans = KMeans(n_clusters=i, init='k-means++', random_state=29, n_jobs=-1)
	#	kmeans.fit(X)
	#	wcss.append(kmeans.inertia_)

	#plt.plot(range(1,11), wcss)
	#plt.title("The Elbow Method")
	#plt.xlabel("Number of clusters")
	#plt.ylabel("WCSS")
	#plt.show()

	#kmeans = KMeans(n_clusters=3, init='k-means++', random_state=29, n_jobs=-1)
	#kmeans.fit(X)

	X_resampled, y_resampled = SMOTE().fit_sample(X, y)
	#clf_smote = LinearSVC().fit(X_resampled, y_resampled)

	rfc = RandomForestClassifier(n_estimators=50)
	#rfc.fit(X_train,y_train)

	scores = cross_val_score(rfc, X_resampled, y_resampled, scoring = "accuracy", cv=10)
	#predict = rfc.predict(X_test)
	#print classification_report(y_test, predict)


	print scores.mean()
	

zoo  = pd.read_csv("parkinsonOriginal.csv")
zoo.head()
cogOs(zoo)