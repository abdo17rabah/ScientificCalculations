import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.ndimage
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform



im= sc.ndimage.imread("dameNB.png") # lire image
#plt.figure()
#plt.imshow(im, cmap='gray')
#plt.show()

def hist(im) :
	x,h=np.unique(im,return_counts=True)
	plt.fill_between(x,0,h)
	plt.axis((0,255,0,np.max(h)))
	plt.show()

#hist=hist(im)

im_bin=im
im_bin[im_bin>230]=255
im_bin[im_bin<=230]=0
#plt.imshow(im_bin, cmap='gray')
#plt.show()

coor=np.argwhere(im_bin==255)
print(coor)
print(coor.shape)
v=pdist(coor.T, "euclidean")
print(v)
m=squareform(v)
print(m)
#sc.misc.imsave("tigre_modifie.png",image)
