#CODIGO REALIZADO POR HECTOR TORIBIO GONZALEZ
import numpy as np

import copy

import seaborn as sb

import matplotlib.pyplot as plt

import time

from SyncRNG import SyncRNG

from queue import PriorityQueue

#CLASE EJE EN LA QUE SE ALMACENA UN NODO Y EL PESO DE ESE NODO

class eje:
        def __init__(self, nodo, peso):
            self.nod = nodo
            self.peso = peso
        
        def toString(self):
            print("V:" , self.nod.compNum(), " P:", self.peso, "||", end = "")
        
        def setPeso(self, x):
            self.peso = x
        
        def getPeso(self):
            return self.peso
        
        def setNodo(self, y):
            self.nod = y
        
        def getNodo(self):
            return self.nod
        
        def getTodo(self):
            return self.nod, self.peso


#CLASE NODO QUE ALMACENA EL NUMERO DE NODO Y SI ESTA O NO VISITADO

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

#GENERA EL GRAFO EN FORMA DE LISTA INTRODUCIENDO EN CADA POSICION DE LA LISTA LOS EJES QUE TIENE EL NODO CORRESPONDIENTE A ESA POSICION

def generaLista(f, c, sem, sem2, prob, E, V):
    num = SyncRNG(seed = sem)
    num2 = SyncRNG(seed = sem2)
    for i in range((f)):
        for j in range((c)):
            if(i>0 and num.rand()<prob):
                rand = num2.randi() % 12 + 1
                E[id(i, j, c)].append(eje(V[id(i-1, j, c)], rand))
                E[id(i-1, j, c)].append(eje(V[id(i, j, c)], rand))
            if(j>0 and num.rand()<prob):
                rand = num2.randi() % 12 + 1
                E[id(i, j, c)].append(eje(V[id(i, j-1, c)], rand))
                E[id(i, j-1, c)].append(eje(V[id(i, j, c)], rand))
    return E


#IMPRIME LA MATRIZ E, USADO PARA COMPROBACIONES

def imprimeEjes(E, fil, col):
    for i in range (0,fil):
        for j in range (0, col*fil):
            print(E[i][j], " " , end="")
        print("\n")

#RELLENA EL ARRAY V CON NODOS NO VISITADOS

def rellenanodos(V, fil, col):

    for i in range(0, fil*col):
        V[i] = nodo(i, False)
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


#METODO QUE RECORRE LA MATRIZ QUE SE PINTA COMPROBANDO EN QUE POSICIONES SE TIENE QUE PINTAR EL LABERINTO, PARA LISTAS

def recorreLista(V, E, fil, col, sal, des, camino1, tent1, camino2, tent2):
    matrizPinta = np.zeros(((fil*2)+1,(col*2)+1))
    for i in range(0,(fil)):
        for j in range(0,(col)):
            
            #SI EN EL ARRAY DE DISTANCIAS DEL PRIMER CAMINO HAY UN VALOR QUE NO SEA INFINITO, SE PINTA LO QUE HAYA EN ESE ARRAY
            if(tent1[id(i, j, c)] != -1):
                matrizPinta[i*2+1][j*2+1] = tent1[id(i,j,c)]
            #SI EN EL ARRAY DE DISTANCIAS DEL OTRO CAMINO HAY UN VALOR QUE NO SEA INFINITO, SE PINTA LO QUE HAYA EN ESE ARRAY
            elif(tent2[id(i, j, c)] != -1):
                matrizPinta[i*2+1][j*2+1] = tent2[id(i,j,c)]
            #SI HAY INFINITO EN LOS DOS, SINGNIFICA QUE AHI TIENE QUE HABER UN INFINITO ASI QUE PINTAMOS UN -1
            #ESTA ESTRUCTURA DE IF Y ELSES LA HACEMOS CADA VEZ QUE TENEMOS QUE PINTAR EN ESTE METODOS PARA PINTAR LO QUE CORRESPONDE DE CADA CAMINO
            else:
                matrizPinta[i*2+1][j*2+1] = -1
            array =[]
            for v in range(0, len(E[id(i,j,c)])):
                array.append(E[id(i,j,c)][v].getNodo().compNum())
            if((i<f-1) and id(i+1,j,c) in array):

                #REPETIMOS ESTRUCTURA DE IF Y ELSE
                if(tent1[id(i+1, j, c) != -1]):
                    matrizPinta[ i*2+2 ][ j*2+1 ] = tent1[id(i+1,j,c)]
                elif(tent2[id(i+1, j, c) != -1]):
                    matrizPinta[ i*2+2 ][ j*2+1 ] = tent2[id(i+1,j,c)]
                else:
                    matrizPinta[ i*2+2 ][ j*2+1 ] = -1
            array =[]
            for v in range(0, len(E[id(i,j,c)])):
                array.append(E[id(i,j,c)][v].getNodo().compNum())
            if((j<c-1) and id(i,j+1,c) in array):

                #REPETIMOS ESTRUCTURA DE IF Y ELSE
                if(tent1[id(i, j+1, c) != -1]):
                    matrizPinta[ i*2+1 ][ j*2+2 ] = tent1[id(i,j+1,c)]
                elif(tent2[id(i, j+1, c) != -1]):
                    matrizPinta[ i*2+1 ][ j*2+2 ] = tent2[id(i,j+1,c)]
                else:
                    matrizPinta[ i*2+1 ][ j*2+2 ] = -1
    
    
    
    #PINTAMOS EN CADA PASILLO EL MENOR PESO DE LOS NODOS QUE LE COMPONEN
    for i in range(0, len(E)-1):
        for j in range (0, len(E[i])):
            #SI ESTAMOS EN EL PRIMER CMAINO
            if(tent1[i] != -1 and tent1[E[i][j].getNodo().compNum()] != -1):
                color = []
                color.append(tent1[i])
                color.append(tent1[E[i][j].getNodo().compNum()])
                minimo = np.min(color)
                matrizPinta[int((((fila(i,col))*2+1)+((fila(E[i][j].getNodo().compNum(),col))*2+1))/2)][int((((columna(i,col))*2+1)+((columna(E[i][j].getNodo().compNum(),col))*2+1))/2)] = minimo
            
            #SI ESTAMOS EN EL OTRO CAMINO
            elif(tent2[i] != -1 and tent2[E[i][j].getNodo().compNum()] != -1):
                color = []
                color.append(tent2[i])
                color.append(tent2[E[i][j].getNodo().compNum()])
                minimo = np.min(color)
                matrizPinta[int((((fila(i,col))*2+1)+((fila(E[i][j].getNodo().compNum(),col))*2+1))/2)][int((((columna(i,col))*2+1)+((columna(E[i][j].getNodo().compNum(),col))*2+1))/2)] = minimo
            
            #SI EN LOS DOS NODOS HAY INFINITO, PINTAMOS EL PASILLO INFINITO
            else:
                matrizPinta[int((((fila(i,col))*2+1)+((fila(E[i][j].getNodo().compNum(),col))*2+1))/2)][int((((columna(i,col))*2+1)+((columna(E[i][j].getNodo().compNum(),col))*2+1))/2)] = -1

    #PINTAMOS LOS NODOS DE LOS CAMINOS

    for k in range(len(camino1)):
        matrizPinta[int((fila(camino1[k],c)))*2+1][int((columna(camino1[k],c)))*2+1] = 500

    for k in range(len(camino2)):
        matrizPinta[int((fila(camino2[k],c)))*2+1][int((columna(camino2[k],c)))*2+1] = 500








    #PINTAMOS LOS PASILLOS DE LOS CAMINOS
    for m in range(len(camino1)-1):
        matrizPinta[int((((fila(camino1[m],c))*2+1)+((fila(camino1[m+1],c))*2+1))/2)][int((((columna(camino1[m],c))*2+1)+((columna(camino1[m+1],c))*2+1))/2)] = 500
    
    for m in range(len(camino2)-1):
        matrizPinta[int((((fila(camino2[m],c))*2+1)+((fila(camino2[m+1],c))*2+1))/2)][int((((columna(camino2[m],c))*2+1)+((columna(camino2[m+1],c))*2+1))/2)] = 500
    
    #PINTAMOS LA POSICION DE SALIDA Y LA DE LLEGADA DISTINTO
    matrizPinta[fila(sal.compNum(),c)*2+1][columna(sal.compNum(),c)*2+1] = 130
    matrizPinta[fila(des.compNum(),c)*2+1][columna(des.compNum(),c)*2+1] = 130

    return matrizPinta


#ALGORITMO DE DIJKSTRA BIDIRECCIONAL, ES COMO EL DIJKSTRA NORMAL PERO DUPLICANDO MUCHAS DE LAS COSAS Y RECORRIENDOLO EN IDA Y VUELTA A LA VEZ HASTA QUE CHOQUEN
def bidirDijkstra(V, E, salida, llegada):
    #INICIALIZAMOS DICCIONARIO DE DISTANCIAS, DICCIOANRIO DE PADRES, ARRAY EN EL QUE GUARDAMOS EL CAMINO, TODO POR DUPLICADO
    D = {}
    D2 = {}
    D[salida.compNum()] = 0
    D2[llegada.compNum()] = 0
    padre = {}
    padre2 = {}

    #DICCIONARIO PARA GUARDAR LOS NODOS DE DISTANCIA MINIMA DE LA IDA PARA SALID DEL BUCLE CUANDO LOS CAMINOS CHOQUEN
    recorridas = {}
    comprueba = []
    comprueba2 = []
    cola = PriorityQueue()   
    cola2 = PriorityQueue()                            

    for v1 in V:
        if V[v1].compNum() != salida.compNum():
            D[V[v1].compNum()] = 999999
        cola.put((D[V[v1].compNum()], V[v1].compNum()))

        if V[v1].compNum() != llegada.compNum():
            D2[V[v1].compNum()] = 999999
        cola2.put((D2[V[v1].compNum()], V[v1].compNum()))
    

    #MIENTRAS LAS DOS COLAS ESTEN LLENAS
    while cola and cola2:

        #SACAMOS LOS NODOS CORRESPONDIENTES A LAS DISTANCIAS MINIMAS
        distancia_min = cola.get()[1]
        distancia_min2 = cola2.get()[1]

        #METEMOS EL NODO DE DISTANCIA MINIMA DE LA COLA DE IDA EN EL DICCIONARIO DE RECORRIDAS
        recorridas[distancia_min] = distancia_min

        #COMPROBAMOS SI EL NODO DE LA SEGUNDA COLA POR EL QUE NOS LLEGAMOS COINCIDE CON ALGUNO DEL DICCIONARIO DE RECORRIDAS
        #, EN EL CASO DE QUE COINCIDA SE SALE DEL BUCLE PORQUE YA SE HAN CHOCADO LOS CAMINOS
        if(distancia_min2 in recorridas.keys()):
            print(distancia_min2)
            corte = distancia_min2
            break

        
        options = E[distancia_min]
        options2 = E[distancia_min2]                    

        #RECORREMOS LOS HIJOS DE LOS NODOS DE DISTANCIA MINIMA
        for hijos in options:
            if hijos.getPeso() + D[distancia_min] < D[hijos.getNodo().compNum()]:
                D[hijos.getNodo().compNum()] = hijos.getPeso() + D[distancia_min]
                padre[hijos.getNodo().compNum()] = distancia_min
                cola.put((D[hijos.getNodo().compNum()], hijos.getNodo().compNum()))

        for hijos in options2:
            if hijos.getPeso() + D2[distancia_min2] < D2[hijos.getNodo().compNum()]:
                D2[hijos.getNodo().compNum()] = hijos.getPeso() + D2[distancia_min2]
                padre2[hijos.getNodo().compNum()] = distancia_min2
                cola2.put((D2[hijos.getNodo().compNum()], hijos.getNodo().compNum()))

        #SI NO SE HAN ENCONTRADO Y HAN TERMINADO SE SALE DEL BUCLE
        if(distancia_min == llegada.compNum() or distancia_min2 == salida.compNum()):
                break
        
    #MOMENTO EN EL QUE HACMOS EL BACKTRACKING PARA SACAR EL CAMINO, VAMOS HACIA ATRAS METIENDO LOS NODOS DEL CAMINO EN EL ARRAY DE CAMINOS 
    #DESDE EL PUNTO DE CORTE HASTA QUE LLEGUEMOS AL PUNTO EN EL QUE SALIDA Y DESPUES DESDE EL PUNTO DE CORTE HASTA LA LLEGADA 
    nodoAct = distancia_min2
    nodoAct2 = distancia_min2
    
    while nodoAct != salida.compNum():

        comprueba.insert(0, nodoAct)
        nodoAct = padre[nodoAct]
    comprueba.insert(0, salida.compNum())

    while nodoAct2 != llegada.compNum():

        comprueba2.insert(0, nodoAct2)
        nodoAct2 = padre2[nodoAct2]
    comprueba2.insert(0, llegada.compNum())


    return comprueba,D, comprueba2, D2, corte


def bidirAestrella(V, E, salida, llegada, col):
    #INICIALIZAMOS DICCIONARIO DE DISTANCIAS, DICCIOANRIO DE PADRES, ARRAY EN EL QUE GUARDAMOS EL CAMINO, TODO POR DUPLICADO
    D = {}
    D2 = {}
    D[salida.compNum()] = 0
    D2[llegada.compNum()] = 0
    padre = {}
    padre2 = {}

    #DICCIONARIO PARA GUARDAR LOS NODOS DE DISTANCIA MINIMA DE LA IDA PARA SALID DEL BUCLE CUANDO LOS CAMINOS CHOQUEN
    recorridas = {}
    comprueba = []
    comprueba2 = []
    cola = PriorityQueue()   
    cola2 = PriorityQueue()                            

    for v1 in V:
        if V[v1].compNum() != salida.compNum():
            D[V[v1].compNum()] = 999999
        cola.put((D[V[v1].compNum()], V[v1].compNum()))
    
    for v2 in V:
        if V[v2].compNum() != llegada.compNum():
            D2[V[v2].compNum()] = 999999
        cola2.put((D2[V[v2].compNum()], V[v2].compNum()))
    

    #MIENTRAS LAS DOS COLAS ESTEN LLENAS
    while cola and cola2:

        #SACAMOS LOS NODOS CORRESPONDIENTES A LAS DISTANCIAS MINIMAS
        distancia_min = cola.get()[1]
        distancia_min2 = cola2.get()[1]

        #METEMOS EL NODO DE DISTANCIA MINIMA DE LA COLA DE IDA EN EL DICCIONARIO DE RECORRIDAS
        recorridas[distancia_min] = distancia_min

        #COMPROBAMOS SI EL NODO DE LA SEGUNDA COLA POR EL QUE NOS LLEGAMOS COINCIDE CON ALGUNO DEL DICCIONARIO DE RECORRIDAS
        #, EN EL CASO DE QUE COINCIDA SE SALE DEL BUCLE PORQUE YA SE HAN CHOCADO LOS CAMINOS
        if(distancia_min2 in recorridas.keys()):
            corte =  distancia_min2
            print(distancia_min2)
            break

        
        options = E[distancia_min]
        options2 = E[distancia_min2]                    

        #RECORREMOS LOS HIJOS DE LOS NODOS DE DISTANCIA MINIMA
        for hijos in options:
            if hijos.getPeso() + D[distancia_min] < D[hijos.getNodo().compNum()]:
                D[hijos.getNodo().compNum()] = hijos.getPeso() + D[distancia_min]
                padre[hijos.getNodo().compNum()] = distancia_min
                #SUMAMOS DISTANCIA DE MANHATTAN
                cola.put((D[hijos.getNodo().compNum()] + manhattan(hijos.getNodo().compNum(), llegada.compNum(), col), hijos.getNodo().compNum()))

        for hijos in options2:
            if hijos.getPeso() + D2[distancia_min2] < D2[hijos.getNodo().compNum()]:
                D2[hijos.getNodo().compNum()] = hijos.getPeso() + D2[distancia_min2]
                padre2[hijos.getNodo().compNum()] = distancia_min2
                #SUMAMOS DISTANCIA DE MANHATTAN
                cola2.put((D2[hijos.getNodo().compNum()] + manhattan(hijos.getNodo().compNum(), salida.compNum(), col), hijos.getNodo().compNum()))


        #SI NO SE HAN ENCONTRADO Y HAN TERMINADO SE SALE DEL BUCLE
        if(distancia_min == llegada.compNum() or distancia_min2 == salida.compNum()):
                break
        
    #MOMENTO EN EL QUE HACMOS EL BACKTRACKING PARA SACAR EL CAMINO, VAMOS HACIA ATRAS METIENDO LOS NODOS DEL CAMINO EN EL ARRAY DE CAMINOS 
    #DESDE EL PUNTO DE CORTE HASTA QUE LLEGUEMOS AL PUNTO EN EL QUE SALIDA Y DESPUES DESDE EL PUNTO DE CORTE HASTA LA LLEGADA
    nodoAct = distancia_min2
    nodoAct2 = distancia_min2
    
    while nodoAct != salida.compNum():

        comprueba.insert(0, nodoAct)
        nodoAct = padre[nodoAct]
    comprueba.insert(0, salida.compNum())

    while nodoAct2 != llegada.compNum():

        comprueba2.insert(0, nodoAct2)
        nodoAct2 = padre2[nodoAct2]
    comprueba2.insert(0, llegada.compNum())


    return comprueba,D, comprueba2, D2, corte

#METODO QUE SACA LA DISTANCIA DE MANHATTAN DE DOS NODOS QUE SE LE PASEN, EN ESTE CASO PASAMOS EL NODO POR EL QUE NOS LLEGAMOS Y EL NODO FINAL

def manhattan(nodo, llegada,col):

    #SACAMOS COMPONENTES DEL NODO POR EL QUE NOS LLEGAMOS
    nodo_x = fila(nodo, col)
    nodo_y = columna(nodo, col)

    #SACAMOS COMPONENTES DEL NODO FINAL
    llegada_x = fila(llegada, col)
    llegada_y = columna(llegada, col)

    #RETORNAMOS LA FORMULA DE MANHATTAN
    return (abs(nodo_x - llegada_x) + abs(nodo_y - llegada_y))

def rellenaLista(E, f, c):
    for i in range(0, f*c+1):
        E.append([])
    return E

##################################### MAIN ##########################################

#VARIABLES DE SEMILLA Y PROBABILIDAD
semilla = int(input("\nQue semilla quieres usar para los nodos: "))
semilla2 = int(input("\nQue semilla quieres usar para los ejes: "))
semilla3 = int(input("\nQue semilla quieres usar para la entrada y salida: "))
probabilidad = float(input("\nQue probabilidad quieres usar: "))

#VARIABLES DE NUMERO DE FILAS Y COLUMNAS
f = int(input("\nIntroduce las filas: "))
c = int(input("\nIntroduce las columnas: "))

#INICIALIZACION DE MATRICES Y ARRAYS
V = rellenanodos({}, f, c)

num3 = SyncRNG(seed = semilla3)
salida = V[num3.randi() % len(V)]
destino = V[num3.randi() % len(V)]

print(salida.compNum(), destino.compNum())

#INICIALIZACION DE TIEMPOS
timeIn = 0
timedes = 0

#INICIALIZAMOS Y RELLENAMOS LA LISTA
E = rellenaLista([], f, c)
E = generaLista(f, c, semilla, semilla2, probabilidad, E, V)

#DIJKSTRA, MEDIMOS EL TIEMPO
timeIn = time.time()
#camino1, distancias1, camino2, distancias2, corte = bidirDijkstra(V, E, salida, destino)
camino1, distancias1, camino2, distancias2, corte = bidirAestrella(V, E, salida, destino, c)
timedes = time.time()
#FIN DEL DIJKSTRA

#SUSTITUIMOS TODOS LOS INFINITO POR -1 PARA QUE LO PINTE EN EL SET_UNDER DE VERDE
for i in distancias1:
    if(distancias1[i] == 999999):
        distancias1[i] = -1

for j in distancias2:
    if(distancias2[j] == 999999):
        distancias2[j] = -1

matrizpinta = recorreLista(V, E, f, c, salida, destino, camino1, distancias1, camino2, distancias2)
    
#SACAMOS EL COSTE TOTAL Y LO IMORIMIMOS, LO SACAMOS OBTENIENDO EL COSTE DEL PUNTO DE CORTE EN EL PRIMER ARRAY DE DISTANCIAS Y
# SUMANDOSELO AL COSTE EN EL SEGUNDO ARRAY
print("coste: ", distancias1[corte] + distancias2[corte])
#CALCULO DEL TIEMPO
timeTot = timedes - timeIn
print("\nTiempo de algoritmo: ", timeTot)

cmap=copy.copy(plt.get_cmap("cubehelix"))
cmap.set_under("coral")

sb.heatmap(matrizpinta,vmin=0,cmap=cmap,cbar_kws={'extend': 'min', 'extendrect': True}, annot=None, fmt="")
plt.show()

plt.colorbar()
plt.show()