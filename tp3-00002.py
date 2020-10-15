#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.ndimage
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

def calculDistance (ville1,ville2):
    r=6367.445
    pl1=np.radians(coord[dic[ville1],0])
    pl2=np.radians(coord[dic[ville2],[0]])
    plon1=np.radians(coord[dic[ville1],[1]])
    plon2=np.radians(coord[dic[ville2],[1]])
    dis=r*np.arccos(np.sin(pl1)*np.sin(pl2)+(np.cos(pl1)*np.cos(pl2)*np.cos(plon2-plon1)))
    return dis

def calculCoordonees(ville1):
    r=6367.445
    plat=np.radians(coord[dic[ville1],0])
    plon=np.radians(coord[dic[ville1],[1]])
    x=r*np.cos(plat)*np.sin(plon)
    y=r*np.cos(plat)*np.sin(plon)
    z=r*np.sin(plat)
    return [x,y,z]





nom_ville =np.loadtxt("villes_normandie.csv" ,  delimiter =";" ,dtype=np.string_,usecols=(8,),skiprows=1)

print(nom_ville[4].decode("latin_1"))
print(nom_ville[4])
dic={}
for i in range(len(nom_ville)):
    dic[nom_ville[i].decode("latin_1")]=i
print(dic)
coord = np.loadtxt("villes_normandie.csv" , delimiter =";", usecols =(11,12),skiprows=1)
print(coord)
dis=calculDistance ('Caen','Rouen')
print(dis)

print("Matrice Distance")
v=pdist(coord, "euclidean")
r=6367.445
print(v)
m=squareform(v)
print(m[:100])

caen=calculCoordonees('Caen')
print(caen)
Rouen=calculCoordonees('Rouen')
print(Rouen)  
v=pdist([caen,Rouen], "euclidean") 
print(v) 

x= coord[:,0] #recuperation de la colonne 0
y= coord[:,1] #recuperation de la colonne 1
plt.scatter(x,-y)
plt.title("les villes normandes")
plt.show()  

print(np.histogram(m))
