from gettext import npgettext
import numpy as np 
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from knn import KNN

cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])

iris = datasets.load_iris()

print(iris.target_names)

X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)



clf = KNN(3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
for i, prediction in enumerate(predictions):
    print(iris.target_names[prediction])
# print(predictions)

plt.figure()
plt.scatter(X[:,2], X[:,3], c=y, cmap=cmap, edgecolor='k', s=20)
plt.show()