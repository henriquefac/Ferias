import numpy as np
import math as ma
from colorama import Fore, Back, Style
class matriz():
    def __init__(self, x) -> None:
        self.altura =  x
        self.largura = x
        self.mat = []
        self.criarMatriz()
        self.listaRaiz = []
        self.listaPontos = []


    def criarMatriz(self):
        self.mat = [None]*self.altura
        for i in range(len(self.mat)):
            linha = [None]*self.largura
            for m in range(len(linha)):
                linha[m] = " "
            self.mat[i] = linha


    def criarPontos(self, ponto:tuple, raiz:tuple):
        self.listaPontos.append(ponto)
        self.listaRaiz.append(raiz)



    def criarLinhas(self, ponto:tuple, raiz:tuple):
        
        self.add(raiz)
        coN = ponto[1] - raiz[1]
        caN = ponto[0] - raiz[0]
        co = abs(coN)
        ca = abs(caN)
        
        if ca == 0:
            ca = 1
        angulo = (np.arctan(co/ca))
        hipo = ma.sqrt(ma.pow(co, 2) + ma.pow(ca, 2))

        section = 3
        
        qunt = int(abs(np.divide(hipo, section)))
        array_pontos = []
        for i in range(qunt):
            h = section*(i+1)
            x = np.cos(angulo)*h
            y = np.sin(angulo)*h
            if caN > 0:
                x = abs(round(raiz[0]+x))
            else:
                x = abs(round(raiz[0]-x))
            if coN > 0:
                y = abs(round(raiz[1]+y))
            else:
                y = abs(round(raiz[1]-y))
            self.add((x,y))
            array_pontos.append((x,y))

        



    def add(self, cordenadas:tuple):
        self.mat[self.altura-1 - cordenadas[1]][cordenadas[0]] = "*"



    def show(self):
        linha = ""
        for i in range(len(self.mat)):
            linha += "| "
            for m in range(len(self.mat[0])):
                linha+= self.mat[i][m] +" "
            linha+="|\n"

        print(linha)