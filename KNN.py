import numpy as np
import matplotlib.pyplot as plt
u1=np.array([2,5])
cov1=np.array([[5,4],
               [4,5]])
u2=np.array([6,1])
cov2=np.array([[-2,-3],
               [-3,-2]])
x1=np.random.multivariate_normal(u1,cov1,400)
x2=np.random.multivariate_normal(u2,cov2,200)
y=np.zeros(600)
y[:400]=1
#plt.scatter(x1[:,0] , x1[:,1],label="girls")
#plt.scatter(x2[:,0], x2[:,1],label="boys")
x=np.vstack((x1,x2))
plt.scatter(x[:,0],x[:,1],c=y)
#q=np.array([6,3])
q=np.array([1,2])
def distance(x,y):
    return np.sqrt(sum((x-y)**2))
plt.scatter(q[0],q[1])
def knn(x,y,q,k=100):
    values=[]
    m=x.shape[0]
    for i in range(m):
        d=distance(x[i],q)
        values.append((d,y[i]))
    values.sort()
    vals=values[:k]
    vals=np.array(vals)
    c=np.unique(vals[:,1],return_counts=True)
    index=c[1].argmax()
    pred=c[0][index]
    return pred

plt.show()
l=knn(x,y,q)
print(l)
