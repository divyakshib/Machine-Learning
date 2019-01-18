import numpy as np
import matplotlib.pyplot as plt
u=5
std=2.2
x=(np.random.randn(200)*std+u)
noise=np.random.randn(200)
y=x*2+noise
#print(x)
#plt.hist(x)
plt.scatter(x,y)
plt.show()