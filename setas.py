from matriz import matriz
import numpy as np
import math as ma

#criar linhas a partir de dois pontos



var = 30
mat = matriz(var)

ra = int(abs(var/2) -1)
raiz = (ra,ra)
ponto1 = (var-1,var-1)
ponto2 = (0, var-1)
ponto3 = (0,0)
ponto4 = (var-1,0)





mat.criarLinhas(ponto1, raiz)
mat.criarLinhas(ponto2, raiz)
mat.criarLinhas(ponto3, raiz)
mat.criarLinhas(ponto4, raiz)



mat.show()