#Código realizado por Héctor Toribio González
import numpy as np

import seaborn as sb

import matplotlib.pyplot as plt

import math

import random

import time

def rellenaMatriz(matriz, n, m):
    for i in range(n):
        for j in range(m):
            #x=0+j*(math.pi/(n-1))
            #y=math.pi-i*(math.pi/(m-1))
            x=-4+j*(12/(n-1))
            y=8-i*(12/(m-1))
            #Función semana1
            #matriz[i][j]=y+math.sin(math.pi*math.sqrt(x*x+y*y))
            #Funcion semana2_1
            #matriz[i][j] = math.sin(x) + math.cos(y) + math.sin(x) * math.cos(y) + math.sin(x*2)
            #Funcion semana2_2
            #matriz[i][j] = 2 * math.sin(x) * math.cos(y/2) + x +  math.log( abs(y-math.pi/2))
            #Funcion semana2_3
            #matriz[i][j] = math.sin(x) * math.cos(y) + math.sqrt(x*y)
            #Funcion semana2_4
            #atriz[i][j] = math.sin( x*7 ) + math.cos( (y+math.pi/4)*4 ) + (x+y)

            matriz[i][j] = 2*(-math.sqrt(x*x+y*y)+(math.cos(y)+math.sin(x))*math.sin(y+x)) + 15*(math.sqrt((x+1)*(x+1)+y*y)-1)/((math.sqrt((x+1)*(x+1)+y*y)-1)*(math.sqrt(x*x+y*y)-1)+1)

            


def hillClimb(matriz, n, m, p, posicionesCamino, arrive):
    llega = 0
    no_llega = 0
    valorMax = 0
    
    while(p>0):
        matriz = matriz
        x=random.randrange(0, n)
        y=random.randrange(0, m)
        find=False
    
        while(not find):
            valor=matriz[x][y]
            valorAux = valor
            xSig = x
            ySig = y
            if((x+1)<n):
                if(matriz[x+1][y]>valor):
                    xSig=x+1
                    ySig=y
                    valor=matriz[x+1][y]
            if((x-1)>=0):
                if(matriz[x-1][y]>valor):
                    xSig=x-1
                    ySig=y
                    valor=matriz[x-1][y]
            if((y+1)<m):
                if(matriz[x][y+1]>valor):
                    ySig=y+1
                    xSig=x
                    valor=matriz[x][y+1]
            if((y-1)>=0):
                if(matriz[x][y-1]>valor):
                    ySig=y-1
                    xSig=x
                    valor=matriz[x][y-1]
            if(valorAux == valor):
                find = True
                if(valor == np.max(matriz)):
                    llega+=1
                else:
                    no_llega+=1
                if(valor>valorMax):
                    valorMax = valor

       
            posicionesCamino.append([x, y])
            x = xSig
            y = ySig
        p = p-1
    arrive.append(llega)
    arrive.append(no_llega)
   
        

def recorrer(matriz, n, m):
    i = 0
    valorMax = matriz[0][0]
    while(i<n):
        j = 0
        while(j<m):
            if(valorMax<matriz[i][j]):
                valorMax = matriz[i][j]
            j+=1
        i+=1
    print(valorMax)




filas=input("Introduzca filas: ")
columnas=input("Introduzca columnas: ")
puntos = input("Número de puntos: ")

tRecorre = 0 #Tiempo del normal
tHill = 0 #Tiempo del Voraz

n = int(filas)
m = int(columnas)
p = int(puntos)


matriz=np.zeros((n, m))

inicioR = time.time()
rellenaMatriz(matriz, n, m)
finalR = time.time()
tRecorre = finalR - inicioR
#recorrer(matriz, n, m)


arrive = []
posicionesCamino = []
inicioH = time.time()
hillClimb(matriz, n, m, p, posicionesCamino, arrive)
finalH = time.time()
tHill = finalH - inicioH
print("Veces que se alcanza al máximo: ") 
print(arrive[0])
print("Veces que NO alcanza el máximo: ")
print(arrive[1])
print("Tiempo de recorrer la matriz: ")
print(tRecorre)
print("\nTiempo de HillClimb: ")
print(tHill)

por1 = (arrive[0]/p) * 100
por2 = (arrive[1]/p) * 100
print("Porcentaje de acierto: " + str(por1) + "%")  
print("Porcentaje de acierto: " + str(por2) + "%")  




i = 0

while( i < len(posicionesCamino)-1):
    #print(posicionesCamino[i])
    matriz[posicionesCamino[i][0]][posicionesCamino[i][1]] = np.min(matriz)
    
    i+=1




heat_map = sb.heatmap(matriz, cmap="hot")
plt.show()



