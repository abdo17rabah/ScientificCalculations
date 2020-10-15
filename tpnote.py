#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.ndimage
import scipy.misc
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from scipy.misc import imsave

#---------- Q1 ----------
#La distance entre les deux pions est 2 cases

#---------- Q3 ----------

def affichageImage(img):
   plt.imshow(img, cmap='gray')
   plt.show()

#---------- Q4 ----------
def hist(img):
   temp=img.shape[0]
   x,h=np.unique(img,return_counts=True)
   plt.fill_between(x,0,h)
   plt.axis((0,temp,0,np.max(h)))
   plt.show()
   #return img

#---------- Q5 ----------
def seuillage(img,seuil):
    img[img>seuil]=255
    img[img<=seuil] = 0
    return img

#---------- Q6 ----------
img = sc.ndimage.imread('dameNB.png')
print(img.shape)
affichageImage(img)
#hist=np.zeros((img.shape[0],img.shape[1]))
hist(img)
#hist[:]=np.arange(255)
#sc.misc.imsave('hist.png',hist)
imgbin=seuillage(img,230)
plt.imshow(imgbin, cmap='gray')
plt.show()

#---------- Q7 ----------
imgbin1=seuillage(img,210)
plt.imshow(imgbin1, cmap='gray')
plt.show()

imgbin2=seuillage(img,220)
plt.imshow(imgbin2, cmap='gray')
plt.show()

#---------- Q9 ----------
#Les images sont toutes noires avec l'affichage des pions en blanc

#---------- Partie 3 ----------
#---------- Q1 ----------
coor=np.argwhere(imgbin==255)
#print(coor)
#print(coor.shape)

#---------- Q2 ----------
v=pdist(coor, "euclidean")
print(v)
m=squareform(v)
print(m)

#---------- Q3 ----------
tailleCase=img.shape[0]//7
print(tailleCase)

#temp=np.ones((img.shape[0],img.shape[1]))
#for i in m :
    
#---------- Q4 ----------  
#np.histogram(m)
plt.hist(m, bins='auto')  
plt.title("Histogram" )
plt.show()
 

#Nom : RABAH Abderrafii
#Num Etudiant : 21710554
