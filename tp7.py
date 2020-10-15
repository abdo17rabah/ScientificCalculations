#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.misc
import scipy.ndimage
from PIL import Image
import io

#----------- Partie 1 -----------
#----------- Q3 -----------
im=Image.open("lena.jpg")

#----------- Q4 -----------
im_ref=np.asarray(im, dtype=np.uint8)

#----------- Q5 -----------
#plt.figure()
#plt.imshow(im,cmap='gray',vmin=0,vmax=255)
#plt.show()

#----------- Q6 -----------
im.save('lena2.jpg','JPEG', quality=95, optimize=True,
progressive=True)

#----------- Q7 -----------
im.save('lena3.jpg','JPEG', quality=5, optimize=True,
progressive=True)
#la derniere photo sauvgarder et de mauvaise qualité par rapport à celle de qualité 95 mais elle a une taille inferieure à celle ci(qualité 5 : 8Ko < qualité 95 : 135Ko)

#----------- Q8 -----------
im = Image. open("lena.jpg")
fp = io.BytesIO()
im.save(fp,'JPEG',quality=5,optimize=True,progressive=True)
im_modif = Image. open(fp)
im_modif_numpy = np.asarray(im_modif)
plt.imshow(im_modif_numpy)
plt.show()

#----------- Q9 ----------- 
def degradeImage(im,k):
  if k>0 and k<1:
	k=int (k*100)
	fp = io.BytesIO()
	im.save(fp,'JPEG',quality=k,optimize=True,progressive=True)
	im_modif = Image. open(fp)
	return im_modif

#img = Image. open("dameNB.png")
#img=degradeImage(img,50)
#im_modif_numpy = np.asarray(img)
#plt.imshow(im_modif_numpy)
#plt.show()

#----------- Partie 2 -----------
#----------- Q1 -----------
def psnr(img1,img2) :
	[M N] = np.shape(img1)
	img1=np.asarray(img1)
	img2=np.asarray(img2)
	d=(1/3*M*N)*(np.sum(img1-img2)**2)
	return 10*np.log(255*255/d)


		

