from matriz import matriz
import numpy as np
import math as ma
import os 
import time
var = 32
mat = matriz(var)
var = int((var/2) -1)
#circuferencia
raiz = (var, var)
raio = var


mat.add(raiz)
mat.add((raiz[0] + raio,raiz[1]))

def circuferencia(d):
    degre =d
    rad = np.deg2rad(degre)
    ang = np.deg2rad((180-degre)/2)
    #achar ponto; x

    l = np.divide(np.sin(rad) * raio, np.sin(ang))


    x = raio*np.cos(rad)
    y = np.sqrt(ma.pow(l,2) - ma.pow(raio-x, 2))
    



    if degre == 90:
        x = raiz[0]
        y = raio
    elif degre == 180:
        x = raiz[0] - int(abs(x)) 
        y = raiz[1]
    elif degre == 270:
        x = raiz[0]
        y = raio
    elif degre == 360:
        x = raiz[0] +  int(abs(x)) 
        y = raiz[1]
    elif degre < 90:
        x = int(abs(x)) + raiz[0]
        y = int(abs(y)) + raiz[1]
    elif degre < 180:
        x = raiz[0] - int(abs(x)) 
        y = raiz[1] + int(abs(y))
    elif degre < 270:
        x = raiz[0] - int(abs(x)) 
        y = raiz[1] - int(abs(y))
    elif degre < 360:
        x = raiz[0] + int(abs(x)) 
        y = raiz[1] - int(abs(y))
    mat.criarLinhas((x,y), raiz)
for i in range(0,360, 10):
    os.system("cls")
    circuferencia(i)
    mat.show()
    

#comentário