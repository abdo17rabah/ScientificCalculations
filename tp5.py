#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy.random

#recuperation des cordonnées carthésient des villes normandes
coord_villes = np.load('coord_villes.npy')

#recuperation de la matrice distances entre les villes
d_villes = np.load('d_villes.npy')

def Q3():
    x= coord_villes[:,0] #recuperation de la colonne 0
    y= coord_villes[:,1] #recuperation de la colonne 1
    plt.scatter(x,-y)
    plt.title("Distance entre les villes normandes")
    plt.show()

def Q4():
    x= coord_villes[:,0] #recuperation de la colonne 0
    y= coord_villes[:,1] #recuperation de la colonne 1
    plt.scatter(x,-y,color='b',marker='s',s=5,alpha=0.1) # ces argument permettent de modifier l'apparance des points
    plt.title("Distance entre les villes normandes")
    plt.show()

def Q5():
    #a):
    n=coord_villes.shape[0]
    hasard = np.random.rand(n)
    hasard = hasard<(1/500)

    x1 = coord_villes[:,0]
    y1 = coord_villes[:,1]

    x2 = coord_villes[hasard,0]
    y2= coord_villes[hasard,1]
    

    plt.scatter(x1,-y1,color='b',marker='s',s=5,alpha=0.2)

    plt.scatter(x2,-y2,color='r',marker='s',s=10,alpha=0.7) # ces argument permettent de modifier l'apparance des points
    plt.title("épidemie")
    plt.show()

    return hasard # pour l'utiliser dans la propagation

#----------------------------------------------
#Propagation de la maladie

def propagation():
    s = 4
    n = d_villes.shape[0]
    ville_src = Q5()
    nouvelle_ville_contamine_valeur = s*np.random.randn(n,n)
    nouvelle_ville_contamine = nouvelle_ville_contamine_valeur > d_villes
    nouvelle_ville_contamine = nouvelle_ville_contamine * ville_src
    nouvelle_ville_contamine = np.sum(nouvelle_ville_contamine,axis=1)
    nouvelle_ville_contamine = nouvelle_ville_contamine > 0

    x1 = coord_villes[:,0]
    y1 = coord_villes[:,1]

    x2 = coord_villes[ville_src,0]
    y2 = coord_villes[ville_src,1]

    x3 = coord_villes[nouvelle_ville_contamine,0]
    y3 = coord_villes[nouvelle_ville_contamine,1]

    plt.scatter(x1,-y1,color='b',marker='s',s=5,alpha=0.3)
    plt.scatter(x3,-y3,color='g',marker='s',s=10,alpha=0.7)
    plt.scatter(x2,-y2,color='r',marker='s',s=10,alpha=0.7)
    

    plt.show()
    
    return nouvelle_ville_contamine
