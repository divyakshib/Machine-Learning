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
#plt.scatter(x1[:,0] , x1[:,1],label="girls")
#plt.scatter(x2[:,0], x2[:,1],label="boys")
x=np.vstack((x1,x2))
'''for i in range(600):
    if y[i]==1:
        plt.scatter(x[i,0],x[i,1],color='red')
    else:
        plt.scatter(x[i,0],x[i,1],color='green')'''


#print(x)
#plt.legend()
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()