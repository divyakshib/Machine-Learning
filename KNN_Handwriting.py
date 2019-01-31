import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/home/divyakshi/Downloads/mnist_train.csv')
#plt.scatter(x1[:,0] , x1[:,1],label="girls")
#plt.scatter(x2[:,0], x2[:,1],label="boys")
#q=np.array([6,3])
data=df.values
X=data[:,1:]
Y=data[:,0]
split=int(0.8*X.shape[0])
trainx=X[:split:]
trainy=Y[:split]
testx=X[split:]
testy=Y[split:]

def distance(x,y):
    return np.sqrt(sum((x-y)**2))

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

def draw(sample):
    img=sample.reshape((28,28))
    plt.imshow(img)
    plt.show()
draw(testx[5])
l=knn(trainx,trainy,testx[5])
print(l)



