import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
img=cv2.imread("/home/divyakshi/Desktop/images/download.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
shape=img.shape
allpixels=img.reshape((-1,3))
print(allpixels.shape)
colour=4
km=KMeans(n_clusters=colour)
km.fit(allpixels)
centers=km.cluster_centers_
centers=np.array(centers,dtype='uint8')
print(centers)
plt.imshow(centers)
plt.show()
plt.figure(0,figsize=(8,4))
i=1
grid=[]
for col in centers:
    plt.subplot(1,4,i)
    i+=1
    grid.append(col)
    a=np.zeros((100,100,3),dtype='uint8')
    a[:,:,:]=col
    plt.imshow(a)
plt.show()
new_image=np.zeros((355*500,3),dtype='uint8')
for ix in range(new_image.shape[0]):
    new_image[ix]=grid[km.labels_[ix]]
new_image=new_image.reshape(shape)
plt.imshow(new_image)
plt.show()