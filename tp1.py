import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.misc
import scipy.ndimage
import time

#----------------Les Vecteurs----------------
#v=np.zeros(5)
#print(v)
#print(v.shape)

#u=np.arange(4,12,0.5)
#print(u)
#print(u.shape)

#w=np.arange(-4,5)
#print(w)
#w=w*w
#print(w)
#
#q=np.arange(0,17)
#print(2**q)

#----------------Les Fonctions----------------
#x=np.arange(0,2*np.pi,1e-3)
#y=np.arange(0,2*np.pi,2*np.pi/10)
#fx=np.sin(y)
#plt.plot(y,fx)
#plt.show()

#----------------Q3----------------
#t1=time.time()
#som=0
#for i in range(100000001) :
#	som+=i
#print(som)
#t2=time.time()
#print(t2-t1,'s')

#t3=time.time()
#v=np.arange(100000001)
#print(np.sum(v))
#t4=time.time()
#print(t4-t3,'s')

#----------------Les Matrices----------------
#m=np.zeros((12,4))
#print(m)
#print(m.shape)

#n=np.eye(16)
#print(n)
#print(n.shape)

#q=np.array([[1,31],[51,12]])
#print(q)


#im=sc.misc.ascent()
#m=np.zeros((im.shape[0]+100,im.shape[1]+100))
#m[50:im.shape[0]+50,50:im.shape[1]+50]=im
#plt.imshow(m,cmap='gray',vmin=0,vmax=255)
#plt.figure(2)
#plt.show()

#im = sc.misc.ascent()
im = sc.ndimage.imread('face_gris.png')
#plt.imshow(im,cmap='gray',vmin=0,vmax=255)

#mini=500
#for i in im:
#	for j in i :
#		if j<mini :
#			mini=j
#print(mini)
#
#maxi=0
#for i in im:
#	for j in i :
#		if j>maxi :
#			maxi=j
#print(maxi)
#	
#im2=np.zeros(im.shape)
#for i in im2 :
#	for j in i :
#		for k in im :
#			for l in k : 
#				j=255*((l-mini)/(maxi-mini))
#
print(np.min(im),np.max(im))
im2=255*(im-np.min(im)/np.max(im)-np.min(im))
#plt.imshow(im2,cmap='gray',vmin=0,vmax=255)
plt.show()









