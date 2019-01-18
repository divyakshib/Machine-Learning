import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
X,Y=make_regression(n_samples=200,n_features=1,noise=3.5,random_state=10)
X=X-X.mean()/X.std()
Y=Y.reshape((-1,1))
X=X.reshape((-1,1))
print(Y)
print(X.shape[0])
#plt.show()
ones=np.ones((X.shape[0],1))#to get x*theta+x
X_=np.hstack((X,ones))
def predict(X,theta):
    return np.dot(X,theta)
def closedform(X,Y):
    Y=np.mat(Y)
    first=np.dot(X.T,X)
    second=np.dot(X.T,Y)
    theta=np.linalg.pinv(first)*second
    return theta
theta=closedform(X_,Y)
plt.scatter(X,Y)
plt.plot(X,predict(X_,theta),color="Red")
plt.show()