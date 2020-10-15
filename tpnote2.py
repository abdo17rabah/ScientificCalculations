import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.misc
import scipy.ndimage

#-----------Q2-------------
im = sc.misc.ascent()
im = sc.ndimage.imread('im.png')
plt.imshow(im,cmap='gray',vmin=0,vmax=255)
plt.show()

#-----------Q3-------------
P_out=np.array([[1,0],[1,1],[0,1],[0,0]])

#-----------Q4-------------
m=np.array([[-2,1],[-2,0],[-1,0],[-1,1]])
P_out=P_out+m
print(P_out)

#-----------Q5-6-------------
print(im.shape)
rouge=np.argwhere((im[:,:,0]==255)*(im[:,:,1]==0)*(im[:,:,2]==0))
cyan=np.argwhere((im[:,:,0]==0)*(im[:,:,1]==255)*(im[:,:,2]==255))
vert=np.argwhere((im[:,:,0]==0)*(im[:,:,1]==255)*(im[:,:,2]==0))
bleu=np.argwhere((im[:,:,0]==255)*(im[:,:,1]==0)*(im[:,:,2]==0))
print(rouge)
print(cyan)
print(vert)
print(bleu)
#-----------Q7-------------
P_in=np.zeros((4,2))
P_in[0]=P_in[0][0]+rouge
P_in[1]=P_in[1][1]+cyan
P_in[2]=P_in[2][1]+vert
P_in[3]=P_in[3][1]+bleu
print(P_in)

#-----------Q8-------------
n=np.array([[-73,-311],[-117,-88],[-282,-147],[-73,-311]])
P_in=P_in+n
print(P_in)

#-----------Q9-------------
a = np.zeros((4, 3))
a[0]=a[0,0]+P_in[0]
print(a[0])
#d = np.array([[0,0],[0,0],[0,0]])

#print(np.append(P_in,d,axis=1))

#-----------Partie2.2-------------
#-----------Q1-------------
def loss (W,X_in,X_out):
	return sum((X_out-np.dot(X_in,W))**2)

#-----------Q2-------------
W=np.ones(6).reshape(3,2)
print(W)

#-----------Partie2.3-------------
#-----------Q1-------------
x = np.linspace(-1,1,im.shape[0])
y = np.linspace(-1,1,im.shape[1])
xv, yv = np.meshgrid(x, y)
X=np.append(xv.reshape(-1)[:,np.newaxis],yv.reshape(-1)[:,np.newaxis ], axis=1)

#-----------Q4-------------
indice=np.arange(np.shape[0])

#-----------Q5-------------
indice = indice [(np. abs(newX[:,0])<?)*(np. abs(newX[:,1])<?)]

#Abderrafii RABAH
#21710554