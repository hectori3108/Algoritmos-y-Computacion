#CODIGO REALIZADO POR HECTOR TORIBIO GONZALEZ
import numpy as np

import seaborn as sb

import matplotlib.pyplot as plt

import time

from SyncRNG import SyncRNG

#CLASE NODO EN EL QUE SE ALMACENAN EL NUMERO DE NODO Y SI ESTA O NO VISITADO

class nodo:
        def __init__(self, numero, visitado):
            self.num = numero
            self.vis = visitado
                    
        def toString(self):
            print("N:" , self.num, " V:", self.vis, " Nivel: ", self.niv, "||")
        
        def visitado(self):
            self.vis = not(self.vis)

        def numera(self, n):
            self.num = n
        
        def compVis(self):
            return self.vis
        
        def compNum(self):
            return self.num
   
#METODO QUE IMPRIME LA MATRIZ QUE LE PASES, USADO PARA COMPROBACIONES

def imprimeMatriz(matriz):
    print(len(matriz[1]))
    for i in range(len(matriz)):
        for j in range(0, len(matriz[1])):
            print(matriz[i][j], end=" ")
        print("\n")

#METODO QUE TE DEVUELVE LA FILA PARA LA MATRIZ

def fila(ind, c):
    return int(ind/c)

#METODO QUE TE DEVUELVE LA COLUMNA PARA LA MATRIZ

def columna(ind, c):
    return int(ind%c)

#METODO QUE DEVUELVE LA POSICION EN LA MATRIZ CON NUMERO DE FILA Y COLUMNA    

def id(fil, col, c):
    return fil*c + col

#GENERA EL GRAFO EN FORMA DE LISTA CONCATENANDO LOS NODOS RELACIONADOS

def generaLista(f, c, sem, prob, E):
    V = []
    num = SyncRNG(seed = sem)
    for i in range((f)):
        for j in range((c)):
            if(i>0 and num.rand()<prob):
                E.append(([id(i, j, c)], [id(i-1, j, c)]))
                E.append(([id(i-1, j, c)],[id(i, j, c)]))
            if(j>0 and num.rand()<prob):
                E.append(([id(i, j, c)], [id(i, j-1, c)]))
                E.append(([id(i, j-1, c)], [id(i, j, c)]))
    return E

#GENERA EL GRAFO EN FORMA DE MATRIZ METIENDO UN UNO EN LAS POSICIONES DE NODOS QUE VAN A IR UNIDOS

def generaMatriz(f, c, seed, prob, E):
    num = SyncRNG(seed = seed)
    for i in range((f)):
        for j in range((c)):
            if(i>0 and num.rand()<prob):
                E[id(i, j, c)][id(i-1, j, c)] = 1
                E[id(i-1, j, c)][id(i, j, c)] = 1
            if(j>0 and num.rand()<prob):
                
                E[id(i, j, c)][id(i, j-1, c)] = 1
                E[id(i, j-1, c)][id(i, j, c)] = 1
    return E

#BUSQUEDA POR PROFUNDIDAD EN MATRIZ, LA PILA LA UTILIZO PARA IR ALMACENANDO LAS RELACIONES QUE ME VOY DEJANDO ATRAS PARA LUEGO VOLVER A ELLAS CUANDO LLEGUE A UN NODO SIN
#NINGUNA RELACION, LAS METO EN ORDEN Y VOY MIRANDO LA CABEZA DE LA PILA PARA SABER QUE NODO TENGO QUE MIRAR. "CUELGADE" ES UN ARRAY EN EL QUE GUARDO DE QUE NODO CUELGA
#CADA NODO, ES DECIR, EN LA POSICION 3 DE "CUELGADE" HABRA UN NUMERO QUE SERA EL CORRESPONDIENTE AL NODO DEL QUE CUELGA EL NODO 3.
#CUANDO SE ENCUENTRA UN NODO QUE NO ESTE VISITADO Y QUE ESTE UNIDO AL ACTUAL, ESTE NODO SE INTRODUCE NE LA PILA Y SE MARCA QUE CUELGA DEL NODO ACTUAL

def DFSMatriz(E, V, i, fil, col):
    stack = []
    cuelgade = []
    

    for j in range(0, fil*col):
        cuelgade.append(-5)

    stack.append(i)
    while stack!=[]:
        
        now = stack.pop()
        if not(V[now].compVis()):
            V[now].visitado()
        for key in range (len(V)):
            if not(V[key].compVis()) and E[V[now].compNum()][V[key].compNum()]==1:      #SE MIRA SI EN LA POSICION DE LA MATRIZ HAY UN 1 PARA COMPROBAR LA RELACION ENTRE NODOS
                stack.append(key)
                cuelgade[key] = now
                
    return cuelgade

#BUSQUEDA POR ANCHURA EN MATRIZ, LA PILA LA UTILIZO PARA IR ALMACENANDO LAS RELACIONES QUE ME VOY DEJANDO ATRAS PARA LUEGO VOLVER A ELLAS CUANDO LLEGUE A UN NODO SIN
#NINGUNA RELACION, LAS METO EN ORDEN Y VOY MIRANDO LA PRIMERA POSICION DE LA PILA PARA SABER QUE NODO TENGO QUE MIRAR. "CUELGADE" ES UN ARRAY EN EL QUE GUARDO DE QUE NODO CUELGA
#CADA NODO, ES DECIR, EN LA POSICION 3 DE "CUELGADE" HABRA UN NUMERO QUE SERA EL CORRESPONDIENTE AL NODO DEL QUE CUELGA EL NODO 3.
#CUANDO SE ENCUENTRA UN NODO QUE NO ESTE VISITADO Y QUE ESTE UNIDO AL ACTUAL, ESTE NODO SE INTRODUCE NE LA PILA Y SE MARCA QUE CUELGA DEL NODO ACTUAL

def BFSMatriz(E, V, i, fil, col):
    stack = []
    cuelgade = []

    for j in range(0, fil*col):
        cuelgade.append(-5)

    stack.append(i)
    while stack!=[]:
        now = stack.pop(0)                                                          #DIFERENCIA CON PROFUNDIDAD, SE MIRA LA PRIMERA POSICION EN VEZ DE LA CABEZA DE LA PILA
        if not(V[now].compVis()):
            V[now].visitado()
        for key in range (len(V)):
            if not(V[key].compVis()) and E[V[now].compNum()][V[key].compNum()]==1:      #SE MIRA SI EN LA POSICION DE LA MATRIZ HAY UN 1 PARA COMPROBAR LA RELACION ENTRE NODOS
                stack.append(key)
                cuelgade[key] = now
    return cuelgade

#BUSQUEDA POR PROFUNDIDAD EN LISTA, LA PILA LA UTILIZO PARA IR ALMACENANDO LAS RELACIONES QUE ME VOY DEJANDO ATRAS PARA LUEGO VOLVER A ELLAS CUANDO LLEGUE A UN NODO SIN
#NINGUNA RELACION, LAS METO EN ORDEN Y VOY MIRANDO LA CABEZA DE LA PILA PARA SABER QUE NODO TENGO QUE MIRAR. "CUELGADE" ES UN ARRAY EN EL QUE GUARDO DE QUE NODO CUELGA
#CADA NODO, ES DECIR, EN LA POSICION 3 DE "CUELGADE" HABRA UN NUMERO QUE SERA EL CORRESPONDIENTE AL NODO DEL QUE CUELGA EL NODO 3.
#CUANDO SE ENCUENTRA UN NODO QUE NO ESTE VISITADO Y QUE ESTE UNIDO AL ACTUAL, ESTE NODO SE INTRODUCE NE LA PILA Y SE MARCA QUE CUELGA DEL NODO ACTUAL

def DFSLista(E, V, i, fil, col):
    stack = []
    cuelgade = []
    

    for j in range(0, fil*col):
        cuelgade.append(-5)

    stack.append(i)
    while stack!=[]:
        
        now = stack.pop()
        if not(V[now].compVis()):
            V[now].visitado()
        for key in range (len(V)):
            if not(V[key].compVis()) and (([now], [key]) in E):         #SE MIRA SI EXISTE UNA POSICION DE LA LISTA CON LOS DOS NODOS PARA SABER SI ESTAN RELACIONADOS
                stack.append(key)
                cuelgade[key] = now
                
    return cuelgade

#BUSQUEDA POR ANCHURA EN LISTA, LA PILA LA UTILIZO PARA IR ALMACENANDO LAS RELACIONES QUE ME VOY DEJANDO ATRAS PARA LUEGO VOLVER A ELLAS CUANDO LLEGUE A UN NODO SIN
#NINGUNA RELACION, LAS METO EN ORDEN Y VOY MIRANDO LA PRIMERA POSICION DE LA PILA PARA SABER QUE NODO TENGO QUE MIRAR. "CUELGADE" ES UN ARRAY EN EL QUE GUARDO DE QUE NODO CUELGA
#CADA NODO, ES DECIR, EN LA POSICION 3 DE "CUELGADE" HABRA UN NUMERO QUE SERA EL CORRESPONDIENTE AL NODO DEL QUE CUELGA EL NODO 3.
#CUANDO SE ENCUENTRA UN NODO QUE NO ESTE VISITADO Y QUE ESTE UNIDO AL ACTUAL, ESTE NODO SE INTRODUCE NE LA PILA Y SE MARCA QUE CUELGA DEL NODO ACTUAL
            
def BFSLista(E, V, i, fil, col):
    stack = []
    cuelgade = []
    

    for j in range(0, fil*col):
        cuelgade.append(-5)

    stack.append(i)
    while stack!=[]:
        
        now = stack.pop(0)                                              #DIFERENCIA CON PROFUNDIDAD, SE MIRA LA PRIMERA POSICION EN VEZ DE LA CABEZA DE LA PILA
        if not(V[now].compVis()):
            V[now].visitado()
        for key in range (len(V)):
            if not(V[key].compVis()) and (([now], [key]) in E):         #SE MIRA SI EXISTE UNA POSICION DE LA LISTA CON LOS DOS NODOS PARA SABER SI ESTAN RELACIONADOS
                stack.append(key)
                cuelgade[key] = now
                
    return cuelgade
    
#IMPRIME LA MATRIZ E, USADO PARA COMPROBACIONES

def imprimeEjes(E, fil, col):
    for i in range (0,fil):
        for j in range (0, col*fil):
            print(E[i][j], " " , end="")
        print("\n")

#RELLENA EL ARRAY V CON NODOS NO VISITADOS

def rellenanodos(V, fil, col):
    for i in range(0, fil*col):
        V.append(nodo(i, False))
    return V

#INICIALIZA LA MATRIZ CON 0 -> NODOS SIN RELACIONAR

def inic(fil, col):
    matriz = []
    
    for i in range(0, fil*2+1):
        zeros = []
        for j in range(0, col*2+1):
            zeros.append(0)
        matriz.append(zeros)
    return matriz

#METODO QUE RECORRE LA MATRIZ QUE SE PINTA COMPROBANDO EN QUE POSICIONES SE TIENE QUE PINTAR EL LABERINTO

def recorreMatriz(cuelgade, V, E, fil, col):
    matrizPinta=[]
    matrizPinta=inic(fil,col)
    for i in range(fil):
        for j in range(col):
            
            matrizPinta[i*2+1][j*2+1] = 10
            if(i<fil-1 and E[id(i,j, col)][id(i+1,j,col)] != 0):
                matrizPinta[i*2+2][j*2+1] = 10
            if(j<col-1 and E[id(i, j, col)][id(i, j+1, col)] != 0):
                matrizPinta[i*2+1][j*2+2] = 10
    
    for k in range(len(V)):
        #SI EL NODO ESTA VISITADO
        if(V[k].compVis()):
            #SE PINTA COMO VISITADO
            matrizPinta[fila(V[k].compNum(),col)*2+1][columna(V[k].compNum(),col)*2+1]=20
            #SI EL NODO NO CUELGA DE NADA
            if(cuelgade[V[k].compNum()]==-5):
                #SE ACTUALIZA LA POSICION DEL ARRAY CUELGA
                cuelgade[V[k].compNum()] = V[k].compNum()

            #PARA PINTAR EL CAMINO EN MEDIO DE DOS NODOS SE HACE LA MEDIA DE LAS POSICIONES DE ESTOS DOS
            matrizPinta[int(((fila(V[k].compNum(),col)*2+1)+(fila(cuelgade[k],col)*2+1))/2)][int((((columna(V[k].compNum(),col))*2+1)+(columna(cuelgade[k],col)*2+1))/2)]=20       
    return matrizPinta

#METODO QUE RECORRE LA MATRIZ QUE SE PINTA COMPROBANDO EN QUE POSICIONES SE TIENE QUE PINTAR EL LABERINTO, PARA LISTAS

def recorreLista(cuelgade, V, E, fil, col):
    matrizPinta=[]
    matrizPinta=inic(fil,col)
    for i in range(fil):
        for j in range(col):
            
            matrizPinta[i*2+1][j*2+1] = 10
            if(i<fil-1 and ([id(i,j, col)], [id(i+1,j,col)]) in E):
                matrizPinta[i*2+2][j*2+1] = 10
            if(j<col-1 and ([id(i,j, col)], [id(i,j+1,col)]) in E):
                matrizPinta[i*2+1][j*2+2] = 10

    for k in range(len(V)):
        if(V[k].compVis()):
            matrizPinta[fila(V[k].compNum(),col)*2+1][columna(V[k].compNum(),col)*2+1]=20

            if(cuelgade[V[k].compNum()]==-5):
                cuelgade[V[k].compNum()] = V[k].compNum()

            matrizPinta[int(((fila(V[k].compNum(),col)*2+1)+(fila(cuelgade[k],col)*2+1))/2)][int((((columna(V[k].compNum(),col))*2+1)+(columna(cuelgade[k],col)*2+1))/2)]=20       
    return matrizPinta



##################################### MAIN ##########################################

#VARIABLES DE TIPO DE ESTRUCTURA Y TIPO DE BUSQUEDA
matlis = input("Quieres usar Matriz o Lista (M o L): ")
anprof = input("\nQuieres usar Anchura o Profundidad (A o P): ")

#VARIABLES DE SEMILLA Y PROBABILIDAD
semilla = int(input("\nQue semilla quieres usar: "))
probabilidad = float(input("\nQue probabilidad quieres usar: "))

#VARIABLES DE NUMERO DE FILAS Y COLUMNAS
f = int(input("\nIntroduce las filas: "))
c = int(input("\nIntroduce las columnas: "))

#INICIALIZACION DE MATRICES Y ARRAYS
matrizAd = inic(f*c, c*f)
matrizpinta = inic(f, c)
V = rellenanodos([], f, c)

#INICIALIZACION DE TIEMPOS
timeIn = 0
timeFin = 0

#ESTRUCTURA DE MATRIZ
if(matlis == 'M'):
    E = generaMatriz(f, c, semilla, probabilidad, matrizAd)
    if(anprof == 'P'):
        timeIn = time.time()
        asociaciones = DFSMatriz(E, V, 0, f, c)
        timeFin = time.time()
    else:
        timeIn = time.time()
        asociaciones = BFSMatriz(E, V, 0, f, c)
        timeFin = time.time()
    matrizpinta = recorreMatriz(asociaciones, V, E, f, c)

#ESTRUCTURA DE LISTAS
if(matlis == 'L'):
    E = generaLista(f, c, semilla, probabilidad, matrizAd)
    if(anprof == 'P'):
        timeIn = time.time()
        asociaciones = DFSLista(E, V, 0, f, c)
        timeFin = time.time()
    else:
        timeIn = time.time()
        asociaciones = BFSLista(E, V, 0, f, c)
        timeFin = time.time()
    matrizpinta = recorreLista(asociaciones, V, E, f, c)

#CALCULO FINAL DEL TIEMPO
timeTot = timeFin - timeIn
print("\nTiempo de algoritmo: ", timeTot)

#IMPRESION DE MAPA DE CALOR
plt.imshow(matrizpinta, cmap='YlGnBu', origin='upper')
plt.colorbar()
plt.show()