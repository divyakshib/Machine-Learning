import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
X,Y=make_blobs(n_features=2,n_samples=500,random_state=1,centers=2)
plt.scatter(X[:,0],X[:,1],c=Y)
#plt.show()
def sigmoid(a):
    return 1/(np.exp(-1*a)+1)
def prediction(X,W):
    z=sigmoid(np.dot(X,W))
    return z
def loss(X,Y,W):
    Y_=prediction(X,W)
    cost=np.mean(-Y*np.log(Y_)-(1-Y)*np.log(1-Y_))
    return cost
def update(X,Y,W,learning):
    m=X.shape[0]
    Y_=prediction(X,W)
    dw=np.dot(X.T,Y_-Y)
    W=W-dw*learning/float(m)
    return W
def predict(X,Y,l=0.6,epoch=500):
    one=np.ones((X.shape[0],1))
    X=np.hstack((one,X))
    W=np.zeros((X.shape[1]))
    for i in range(epoch):
        W=update(X,Y,W,l)
        if i%10==0:
            l=loss(X,Y,W)
            print(i, l)
    return W
def get(X,W,label=True):
    one = np.ones((X.shape[0], 1))
    X = np.hstack((one, X))
    prob=prediction(X,W)
    if not label:
        return prob
    else:
        label=np.zeros(prob.shape)
        label[prob>=0.5]=1
        return label

W=predict(X,Y)
print(W)
x1=np.linspace(-1,-10,20)
x2=-(W[0]+W[1]*x1)/W[2]
plt.plot(x1,x2,color='Red')
plt.show()
pred=get(X,W)
acc=np.sum(pred==Y)/X.shape[0]
print(acc)






