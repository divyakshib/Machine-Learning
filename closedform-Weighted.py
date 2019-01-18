import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
X=np.random.random_integers(-100,100,50)
Y=X**5+X**2
X.sort()
Y.sort()
X=X.reshape((-1,1))
Y=Y.reshape((-1,1))
def getWeight(x,point,tau):
    M=x.shape[0]
    W=np.mat(np.eye(M))
    for i in range(M):
        x1=x[i]
        x2=point
        W[i,i] = np.exp(np.dot((x1-x2),((x1-x2).T))/-2*tau*tau)
    return W
def predict(x,y,point,tau):
    M = x.shape[0]
    ones=np.ones((M,1))
    x_=np.stack((x,ones), axis=1)
    point=np.mat([point,1])
    W=getWeight(x,point,tau)
    theta=np.linalg.pinv(x_.T*(W*x_))*x_.T*(W*y)
    pred=np.dot(point,theta)
    return pred
plt.scatter(X,Y,color="Red")
print(predict(X,Y,1,0.7))
res=[]
v=X.tolist()
for j in v:
    for i in j:
        val=j
        print(val)
        #res.append(predict(X,Y,val,0.7))
        print(res)
res=np.asarray(res)
print(res)
plt.scatter(X,res)
plt.show()