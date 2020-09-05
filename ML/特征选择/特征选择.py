from sklearn.feature_selection import VarianceThreshold

x=[[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel=VarianceThreshold(threshold=0.8*0.2)
print(sel.fit_transform(x))


from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest,chi2,SelectFromModel

iris=load_iris()
X,y=iris.data,iris.target
print(X.shape)
X_new=SelectKBest(chi2,k=2).fit_transform(X,y)
print(X_new.shape)

from sklearn.svm import LinearSVC
lsvc=LinearSVC(C=0.01,penalty='l1',dual=False).fit(X,y)
model=SelectFromModel(lsvc,prefit=True)
X_new=model.transform(X)
print(X_new.shape)

from sklearn.tree import ExtraTreeClassifier
clf=ExtraTreeClassifier()
clf.fit(X,y)
print(clf.feature_importances_)
model=SelectFromModel(clf,prefit=True)
X_new=model.transform(X)
print(X_new.shape)


import numpy as np
import matplotlib.pyplot as plt
data=np.random.rand(50000,2)*20+20
data[100:200]+=100
print(min(data[:,0]),max(data[:,0]))
print(min(data[:,1]),max(data[:,1]))
plt.boxplot(data)
plt.show()

