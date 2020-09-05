from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import numpy as np

train_x,train_y=make_classification(n_features=10,n_classes=2,n_samples=100)
train_x=train_x[:,:2]
train_x[:,0]*=5
print(train_x.shape)

def plot_data(X,y,title,ax=None):
    if ax==None:
        ax=plt.gca()
    ax.scatter(X[:,0],X[:,1],s=10,c=y)
    ax.set_title(title)
    ax.set_xlabel('$x_0$')
    ax.set_ylabel("$x_1$")
    ax.grid()
    plt.axis('square')


##################### 归一化 ###################
fig=plt.figure()
ax=fig.add_subplot(1,3,1)
plot_data(train_x,train_y,title='origin data',ax=ax)

ax=fig.add_subplot(1,3,2)
minmaxScaler=MinMaxScaler()
train_x1=minmaxScaler.fit_transform(train_x)
plot_data(train_x1,train_y,title='min max scale',ax=ax)

ax=fig.add_subplot(1,3,3)
stdScaler=StandardScaler()
train_x2=stdScaler.fit_transform(train_x)
plot_data(train_x2,train_y,title='std scale',ax=ax)
plt.show()

######################  特征编码 #########################
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox'],
     ['female', 'from China', 'uses Firefox']]
from sklearn.preprocessing import OrdinalEncoder
enc=OrdinalEncoder()
X1=enc.fit_transform(X)
print(X1)

from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
X2=enc.fit_transform(X)
print(X2)

#################### 离散化 ######################
X = np.array([[ -3., 5., 15 ],
                [  0., 6., 14 ],
                [  6., 3., 11 ]])
from sklearn.preprocessing import KBinsDiscretizer
est=KBinsDiscretizer(n_bins=[3,2,2],encode='ordinal')
X1=est.fit_transform(X)
print(X1)
est=KBinsDiscretizer(n_bins=[3,2,2],encode='onehot')
X1=est.fit_transform(X)
print(X1)

############ 特征二值化 ##################
from sklearn.preprocessing import Binarizer
binarizer=Binarizer().fit(X)
x1=binarizer.transform(X)
print(x1)

