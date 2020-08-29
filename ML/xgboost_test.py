import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import SCORERS
from sklearn.datasets import load_boston
from sklearn.model_selection import cross_val_score,learning_curve,KFold


import matplotlib.pyplot as plt
import numpy as np

dataset=load_boston()
XTrain,YTrain=dataset.data,dataset.target
print(XTrain.shape,YTrain.shape)
XTrain,XTest,YTrain,YTest=train_test_split(XTrain,YTrain,test_size=0.3,random_state=420)


reg=xgb.XGBRegressor(n_estimators=100)
reg.fit(XTrain,YTrain)
y_pred=reg.predict(XTest)
print('MSE:',MSE(YTest,y_pred))
print('Score:',reg.score(XTest,YTest))
print(reg.feature_importances_)

print(SCORERS.keys())
################## 交叉验证 ##############################
reg=xgb.XGBRegressor(n_estimators=100)
xgb_cvs=cross_val_score(reg,XTrain,YTrain,cv=5,scoring='neg_mean_squared_error').mean()
print('xbg cross val score:',xgb_cvs)

# 其他算法
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
linear_cvs=cross_val_score(reg,XTrain,YTrain,cv=5,scoring='neg_mean_squared_error').mean()
print('linear regression cross val score:',linear_cvs)

from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=100)
rf_cvs=cross_val_score(reg,XTrain,YTrain,cv=5,scoring='neg_mean_squared_error').mean()
print('RandomForest regression cross val score:',rf_cvs)


############### 学习曲线 ########################
def plot_learning_curve(estimator,title,X,y,ax=None,ylim=None,cv=None,n_jobs=None):
    train_size,train_score,test_scores=learning_curve(estimator,X,y,shuffle=True,
                                                      random_state=420,
                                                      cv=cv,n_jobs=n_jobs)
    if ax==None:
        ax=plt.gca()
    else:
        ax=plt.figure()
    ax.set_title(title)
    if ylim:
        ax.set_ylim(*ylim)
    ax.set_xlabel('train examples')
    ax.set_ylabel('score')
    ax.grid()
    ax.plot(train_size,np.mean(train_score,axis=1),'o-',c='r',label='train score')
    ax.plot(train_size,np.mean(test_scores,axis=1),'o-',c='g',label='test score')
    ax.legend()
    return ax

cv=KFold(n_splits=5,random_state=42,shuffle=True)
plot_learning_curve(xgb.XGBRegressor(n_estimators=100,random_state=420),'XGB',XTrain,YTrain,cv=cv)
plt.show()  # 过拟合了


axisx=range(10,1010,50)
rs=[]
for i in axisx:
    reg=xgb.XGBRegressor(n_estimators=i,random_state=420)
    rs.append(cross_val_score(reg,XTrain,YTrain,cv=cv).mean())
print(axisx[rs.index(max(rs))],max(rs))
plt.figure()
plt.plot(axisx,rs,'o-',c='r',label='XGB')
plt.xlabel('n_estimators')
plt.ylabel('score')
plt.legend()
plt.show()

######### 进化的学习曲线--方差与泛化误差 ##################
axisx=range(50,1050,50)
rs=[]  # 偏差
var=[] # 方差
ge=[]  # 泛化误差
for i in axisx:
    reg=xgb.XGBRegressor(n_estimators=i,random_state=420)
    cvresult=cross_val_score(reg,XTrain,YTrain,cv=cv)  # R**2 score
    # 记录 1-偏差
    rs.append(cvresult.mean())
    # 记录方差
    var.append(cvresult.var())
    # 记录泛化误差=偏差**2+var
    ge.append((1-cvresult.mean())**2+cvresult.var())
print(axisx[rs.index(max(rs))],max(rs),var[rs.index(max(rs))])
print(axisx[var.index(min(var))],rs[var.index(min(var))],min(var))
print(axisx[ge.index(min(ge))],rs[ge.index(min(ge))],var[ge.index(min(ge))],min(ge))
plt.figure()
plt.plot(axisx,rs,c='red',label='XGB')
plt.legend()
plt.show()

axisx=range(100,300,10)
rs=[]  # 偏差
var=[] # 方差
ge=[]  # 泛化误差
for i in axisx:
    reg=xgb.XGBRegressor(n_estimators=i,random_state=420)
    cvresult=cross_val_score(reg,XTrain,YTrain,cv=cv)  # R**2 score
    # 记录 1-偏差
    rs.append(cvresult.mean())
    # 记录方差
    var.append(cvresult.var())
    # 记录泛化误差=偏差**2+var
    ge.append((1-cvresult.mean())**2+cvresult.var())
print(axisx[rs.index(max(rs))],max(rs),var[rs.index(max(rs))])
print(axisx[var.index(min(var))],rs[var.index(min(var))],min(var))
print(axisx[ge.index(min(ge))],rs[ge.index(min(ge))],var[ge.index(min(ge))],min(ge))
rs=np.array(rs)
var=np.array(var)*0.02
plt.figure()
plt.plot(axisx,rs,c='red',label='XGB')
plt.fill_between(axisx,rs+var,rs-var,facecolor='blue',alpha=0.3)
plt.legend()
plt.show()

import time
time0=time.time()
print(xgb.XGBRegressor(n_estimators=100,random_state=420).fit(XTrain,YTrain).score(XTest,YTest))
print(time.time()-time0)

time0=time.time()
print(xgb.XGBRegressor(n_estimators=660,random_state=420).fit(XTrain,YTrain).score(XTest,YTest))
print(time.time()-time0)

time0=time.time()
print(xgb.XGBRegressor(n_estimators=180,random_state=420).fit(XTrain,YTrain).score(XTest,YTest))
print(time.time()-time0)
