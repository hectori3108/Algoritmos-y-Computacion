#Código realizado por Héctor Toribio González. No tiene implementado las veces que llega o no llega al máximo ya que solo necesitaba sacar los tiempos y ver si me hacía bien los caminos
import numpy as np

import seaborn as sb

import matplotlib.pyplot as plt

import math

import random

import time

#def rellenaMatriz(matriz, n, m):
 #   for i in range(n):
  #      for j in range(m):
            
            #Función semana1
            #matriz[i][j]=y+math.sin(math.pi*math.sqrt(x*x+y*y))
            #Funcion semana2_1
            #matriz[i][j] = math.sin(x) + math.cos(y) + math.sin(x) * math.cos(y) + math.sin(x*2)
            #Funcion semana2_2
            #matriz[i][j] = 2 * math.sin(x) * math.cos(y/2) + x +  math.log( abs(y-math.pi/2))
            #Funcion semana2_3
            #matriz[i][j] = math.sin(x) * math.cos(y) + math.sqrt(x*y)
            #Funcion semana2_4
            #matriz[i][j] = math.sin( x*7 ) + math.cos( (y+math.pi/4)*4 ) + (x+y)
            #Funcion semana3_1
            #matriz[i][j] = math.cos((x*x+y*y)*12)/(2*((x*x+y*y)*6.28+1))
            #Funcion semana3_2
def oper(matriz, i, j, n, m):
    x=-4+j*(12/(n-1))
    y=8-i*(12/(m-1))
    return 2*(-math.sqrt(x*x+y*y)+(math.cos(y)+math.sin(x))*math.sin(y+x)) + 15*(math.sqrt((x+1)*(x+1)+y*y)-1)/((math.sqrt((x+1)*(x+1)+y*y)-1)*(math.sqrt(x*x+y*y)-1)+1)
    


def hillClimb(matriz, n, m, p, posicionesCamino):
    valorMax = 0
    
    while(p>0):
        matriz = matriz
        x=random.randrange(0, n)
        y=random.randrange(0, m)
        find=False
        
        while(not find):
                
                valor= oper(matriz, x, y, n, m)
                valorAux = valor
                xSig = x
                ySig = y
                if((x+1)<n):
                    if(oper(matriz, x+1, y, n, m)>valor):
                        xSig=x+1
                        ySig=y
                        valor=oper(matriz, x+1, y, n, m)
                if((x-1)>=0):
                    if(oper(matriz, x-1, y, n, m)>valor):
                        xSig=x-1
                        ySig=y
                        valor=oper(matriz, x-1, y, n, m)
                if((y+1)<m):
                    if(oper(matriz, x, y+1, n, m)>valor):
                        ySig=y+1
                        xSig=x
                        valor=oper(matriz, x, y+1, n, m)
                if((y-1)>=0):
                    if(oper(matriz, x, y-1, n, m)>valor):
                        ySig=y-1
                        xSig=x
                        valor=oper(matriz, x, y-1, n, m)
                if(valorAux == valor):
                    find = True
                    if(valor>valorMax):
                        valorMax = valor

                if([x,y] in posicionesCamino):
                    find = True
                else:   
                    posicionesCamino.append([x, y])
                
                x = xSig
                y = ySig
               
        p = p-1
    
   
        

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
#arrive = [0,0]

#rellenaMatriz(matriz, n, m)
    #inicioR = time.time()
    #recorrer(matriz, n, m)
    #finalR = time.time()
    #tRecorre = finalR - inicioR
    
posicionesCamino = []
inicioH = time.time()
hillClimb(matriz, n, m, p, posicionesCamino)
finalH = time.time()
tHill = finalH - inicioH
#print("Veces que se alcanza al máximo: ") 
#print(arrive[0])
#print("Veces que NO alcanza el máximo: ")
#print(arrive[1])
#print("Tiempo de recorrer la matriz: ")
#print(tRecorre)
print("\nTiempo de HillClimb: ")
print(tHill)

print("\nTiempo de rellenado: ")
print("0")

#por1 = (arrive[0]/10000) * 100
#por2 = (arrive[1]/10000) * 100
#print("Porcentaje de acierto: " + str(por1) + "%")  
#print("Porcentaje de fallo: " + str(por2) + "%")  

i = 0

while( i < len(posicionesCamino)-1):
    matriz[posicionesCamino[i][0]][posicionesCamino[i][1]] = -10
    
    i+=1



heat_map = sb.heatmap(matriz, cmap="hot")
plt.show()