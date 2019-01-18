import numpy as np
import matplotlib.pyplot as plt
u1=np.array([2,5])
cov1=np.array([[1,2],
               [1,0]])
u2=np.array([6,1])
cov2=np.array([[-1,-1],[0,1]])
x1=np.random.multivariate_normal(u1,cov1,400)
x2=np.random.multivariate_normal(u2,cov2,200)
y=np.zeros(600)
y[:400]=1
x=np.vstack((x1,x2))
'''for i in range(600):
    if y[i]==1:
        plt.scatter(x[i,0],x[i,1],color='red')
    else:
        plt.scatter(x[i,0],x[i,1],color='green')'''
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()
def hypothsis(x,w,b):
    h=np.dot(x,w)+b
    return sigmoid(h)
def sigmoid(z):
    return 1.0/(1.0+np.exp(-1.0*z))
def error(y_,x,w,b):
    m=x.shape[0]
    er=0
    for i in range(m):
        hx=hypothsis(x[i],w,b)
        er+=y_[i]*np.log2(hx)+(1-y)*np.log2(1-hx)
    return -er/m
def grd(y_,x,w,b):
    grad_w=np.zeros(w.shape)
    grad=0.0
    m=x.shape[0]
    for i in range(m):
        hx=hypothsis(x[i],w,b)
        grad_x=-1*(y_[i]-hx)*x[i]
        grad=-1*(y_[i]-hx)
    grad_w/=m
    grad/=m
    return [grad_w,grad]
def gradient_descent(x,y_,w,b,l=0):
    err=error(y_,x,w,b)
    [gw,gb]=grd(y_,x,w,b)
    w=w+l*gw
    b=b+l*gb
    return err,w,b
W=y**2
b=y**3
err,w,b=gradient_descent(x[:,0],x[:,1],W,b)
print(err)