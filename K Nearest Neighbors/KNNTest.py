import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

cmap = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)


from KNN import KNN
clf=KNN(k=3)
clf.fit(X_train,y_train)
predictions=clf.predict(X_test)
acc=np.sum(predictions==y_test)/len(y_test)
print(acc)