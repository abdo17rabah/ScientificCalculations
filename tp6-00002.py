#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.misc
import scipy.ndimage
from mpl_toolkits.mplot3d import Axes3D

#----------- Partie 1.1 -----------
#----------- Q1-2-3 -----------
x=np.arange(-np.pi,np.pi,1e-1)
fx=np.sin(x)
plt.figure()
plt.plot(x,fx)
plt.show()

#----------- Q4 -----------
df1=sc.misc.derivative(np.sin,x,dx=1e-6)
plt.figure()
plt.plot(x,df1)
plt.show()

#----------- Q5 -----------
df2=np.gradient(fx,10e-1)
plt.figure()
plt.plot(x,df2)
plt.show()

#----------- Q6 -----------
df=np.gradient(fx)
#plt.figure()
plt.plot(x,df)

#----------- Partie 1.2 -----------
#----------- Q1 -----------
i=np.arange(len(x))%3 == 0
print(i)

#----------- Q2 -----------
x3=[]
fx3=[]
df3=[]
temp=fx.shape[0]
k=0
while k<temp :
	x3.append(x[k])
	fx3.append(fx[k])
	df3.append(df[k])
	k+=3
x3=np.array(x3)
fx3=np.array(fx3)
df3=np.array(df3)

#----------- Q3 -----------
plt.quiver(x3,fx3,df3,0)
#plt.quiver(x[i],fx[i],df1[i],0)
plt.figure()
plt.plot(x[df>0],fx[df>0])
plt.show()

#La fonction dérivée d'une fonction f(x) ou "dérivée" est la #pente de la tangente au graphe au point de coordonnées [x,f(x)].

#----------- Partie 2.1 -----------
#----------- Q1 -----------
#k=1
x=np.arange(-np.pi,np.pi,1e-1)
fx=np.sin(x)
im = (128*fx[:,np.newaxis].dot(fx[np.newaxis,:])+128)
plt.figure()
plt.imshow(im,cmap='gray',vmin=0,vmax=255)
plt.show()

#----------- Q2 -----------
plt.figure()
plt.plot(im[15]) #bleu
plt.plot(im[30]) #vert
plt.plot(im[45]) #rouge
plt.show()

#----------- Q3 -----------
xx = np.arange(0,im.shape[0])
X,Y = np.meshgrid(xx,xx)
fig = plt.figure()
ax = fig.gca( projection ='3d')
surf = ax.plot_surface(X, Y, im, linewidth=0, antialiased =True,cmap='gray')
ax.view_init(elev=60.,azim=20)
plt .show()

#----------- Q4 -----------
imGradX,imGradY=np.gradient(im)

#----------- Q5 -----------
xx = np.arange(0,im.shape[0])
X, Y = np.meshgrid(xx,xx)
X=X.reshape(-1)
Y=Y.reshape(-1)
plt.figure()
plt.imshow(im,cmap='gray',vmin=0,vmax=255)
plt.quiver(X,Y,imGradX[X,Y],-imGradY[X,Y],scale=3e2)
#−imGradY car l axe des ordonnées est inversé pour les images.
plt.show()

#----------- Partie 2.2 -----------
#----------- Q1 -----------
def degrade(angle):
	im = np.arange(0,100)*255//100
	im = im*np.ones((100,1))
	im = sc.ndimage.interpolation.rotate(im,angle-90,reshape=False,mode='reflect')
	return im

#----------- Q2 -----------
im1=degrade(30)
im2=degrade(-70)
im3=degrade(10)
plt.figure()
plt.imshow(im1,cmap='gray',vmin=0,vmax=255)
plt.show()
plt.imshow(im2,cmap='gray',vmin=0,vmax=255)
plt.show()
plt.imshow(im3,cmap='gray',vmin=0,vmax=255)
plt.show()

#----------- Q3 -----------
imGradX1,imGradY1=np.gradient(im1)
imGradX2,imGradY2=np.gradient(im2)
imGradX3,imGradY3=np.gradient(im3)

#----------- Q4 -----------
ang1=np.arctan(imGradY1/imGradX1)*180/np.pi
ang2=np.arctan(imGradY2/imGradX2)*180/np.pi
ang3=np.arctan(imGradY3/imGradX3)*180/np.pi
print("ang1",ang1)
print("ang2",ang2)
print("ang3",ang3)

print("-----Moyenne-----")
angle1=np.mean(np.arctan(imGradY1/imGradX1)*180/np.pi)
angle2=np.mean(np.arctan(imGradY2/imGradX2)*180/np.pi)
angle3=np.mean(np.arctan(imGradY3/imGradX3)*180/np.pi)
print("angle1",angle1)
print("angle2",angle2)
print("angle3",angle3)





































