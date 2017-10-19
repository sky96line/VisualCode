'''
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.00001, C=100)

x, y = digits.data[:-10], digits.target[:-10]

clf.fit(x,y)

p = clf.predict([digits.data[-2]])

plt.imshow(digits.images[-2], cmap=plt.cm.gray_r)
plt.show()

==================================================

import numpy as np
from s
klearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

clf = clf.fit(x_train, y_train)

pred = clf.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))
'''

'''
from  sklearn import tree

features = [[140, 1],[130, 1],[150, 0],[170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[150, 0]]))
'''
