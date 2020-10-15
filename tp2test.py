#tp 2
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.misc
import scipy.ndimage
import time


im = sc.misc.ascent()
face_gris = sc.ndimage.imread('face_gris.png') #image face_gris de moodle

def hist (im):
    x,h = np.unique(im,return_counts=True)
    plt.fill_between(x,0,h)
    plt.axis((0,255,0, np.max(h)))
    plt.show()

def eclair(im):
    im2=np.array(im)
    im2[im2+50<=255]+=50
    im2[im2+50>255] = 255
    return im2


def assombrir(im):
    im2 = np.array(im)#np.array(im)
    im2[im2-60>=0]-=60
    im2[im2-60<0] = 0
    return im2


def pMin(im):
    mini = 1000000000000
    for ligne in im:
        for valeur in ligne:
            if valeur < mini:
                mini=valeur
    return mini


def pMax(im):
    maxi = 0
    for ligne in im:
        for valeur in ligne:
            if valeur > maxi:
                maxi = valeur
    return maxi


def question4_3(im):
    t1=time.time()
    new_image = np.zeros(im.shape)
    mini = pMin(im)
    maxi = pMax(im)
    for i in range(len(im)):
        for j in range(len(im[i])):
            new_image[i][j] = 255 * ((im[i][j]-mini)/maxi-mini)

    t2=time.time()-t1
    print("le temps = :",t2,"secondes")
    
    plt.imshow(new_image,cmap='gray')
    plt.show()
    return new_image

def question4_4(im):
    t1 = time.time()
    new_image = im #np.zeros(im.shape)
    mini = np.min(im)
    maxi = np.max(im)

    new_image[:][:] = 255 * ((im[:][:]-mini)/maxi-mini)
    
    t2=time.time()-t1
    print("le temps = :",t2,"secondes")
    
    plt.imshow(new_image,cmap='gray')
    plt.show()
    
def question5_1():
    x=np.arange(0,1,1e-6)
    y=x
    plt.figure("x=y")
    plt.plot(x,y)

    
    plt.figure("y=0.5*cos((1-x)*PI)+0.5")
    y=0.5*np.cos((1-x)*np.pi)+0.5
    plt.plot(x,y)
    
    plt.show()

##def divise_image(im):
##    im2=im[:][:]/255.0
##    plt.imshow(im2,cmap='gray')
##    plt.show()
    

    
    
plt.figure(1)
plt.imshow(im,cmap='gray',vmin=0,vmax=255)
plt.figure(2)
im2=assombrir(im)
plt.imshow(im2,cmap='gray',vmin=0,vmax=255)
plt.show()

plt.figure(1)
plt.imshow(face_gris,cmap='gray',vmin=0,vmax=255)
plt.figure(2)
hist(face_gris)
plt.show()

