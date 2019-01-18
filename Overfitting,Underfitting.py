import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X=np.random.random_integers(-100,100,50)
Y=X**5+X**2
X.sort()
Y.sort()
X=X.reshape((-1,))
Y=Y.reshape((-1,))
x1=X
x2=X**2
X=np.stack((x1,x2),axis=1)
model=LinearRegression()
model.fit(X,Y)
output=model.predict(X)
plt.plot(X[:,0],output,color="orange")
plt.scatter(X[:,0],Y)
plt.show()
x3=X**3
X[:,1]+=x3[:,0]
model=LinearRegression()
model.fit(X,Y)
output=model.predict(X)
plt.plot(X[:,0],output,color="pink")
plt.scatter(X[:,0],Y)
plt.show()
