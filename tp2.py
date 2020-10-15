import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.misc
import scipy.ndimage

#im=sc.misc.ascent()
im = sc.ndimage.imread('face_gris.png')

def hist(im):
	x,h=np.unique(im,return_counts=True)
	plt.fill_between(x,0,h)
	plt.axis((0,255,0,np.max(h)))
	plt.show()

def eclaircir(im,n):
	if n>=0 and n<=255 :
		im[im==255-n]=255
		im[im+n<=255]+=n
	return im

#def eclaircir(im,n):
#    im[im>=255-n]=255
#    for i in im :
#       for j in i :
#          if j+n <= 255:
#              j+=n
#    return im		
	
def assombrir (im,n) :
	im[im<n]=0
	if im.all()-n>=0:
		im[im>n]=-n
	return im
		
#im=hist(im)
#im2=eclaircir(im,100)
im2=assombrir(im,85)
im2=hist(im2)
