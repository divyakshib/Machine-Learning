import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read(file):
    df=pd.read_csv(file)
    return df.values

X=read("/home/divyakshi/Documents/linearX.csv")
Y=read("/home/divyakshi/Documents/linearY.csv")
X=X.reshape((9,))
Y=Y.reshape((9,))
'''print (x)
print(y)'''
X=(X-X.mean())/(X.std())
Y=(Y-Y.mean())/(Y.std())
def hypothesis(theta,x):
    h=theta[0]+x*theta[1]
    return h
def error(x,y,theta):
    tot=0
    m=x.shape[0]
    for i in range(m):
        tot+=(hypothesis(theta,x[i])-y[i])**2
    return tot


def gradient(theta,x,y):
    grad=np.array([0.0,0.0])
    m=x.shape[0]
    for i in range(m):
        grad[0]+=(hypothesis(theta,x[i])-y[i])
        grad[1]+=(hypothesis(theta,x[i])-y[i])*x[i]
    return grad

def graddescent(x,y,l,n):
    grad=np.array([0.0,0.0])
    theta=np.array([0.0,0.0])
    e=[]
    for i in range(n):
        grad = gradient(theta, x, y)
        cp=error(x,y,theta)
        theta[0]=theta[0]-l*grad[0]
        theta[1]=theta[1]-l*grad[1]
        e.append(cp)
    return theta,e
theta,er =graddescent(X,Y,0.001,353)
print(theta)
plt.scatter(X,Y,edgecolors='r')
plt.plot(X,hypothesis(theta,X))
#plt.plot(er)
plt.show()
