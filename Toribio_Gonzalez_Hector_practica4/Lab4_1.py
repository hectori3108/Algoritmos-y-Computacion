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

                rand = num2.randi() % 12 + 1                                #GENERACION DEL PESO
                E[id(i, j, c)].append(eje(V[id(i-1, j, c)], rand))
                E[id(i-1, j, c)].append(eje(V[id(i, j, c)], rand))
            if(j>0 and num.rand()<prob):

                rand = num2.randi() % 12 + 1                                #GENERACION DEL PESO 
                E[id(i, j, c)].append(eje(V[id(i, j-1, c)], rand))
                E[id(i, j-1, c)].append(eje(V[id(i, j, c)], rand))
    return E


#IMPRIME LA MATRIZ E, USADO PARA COMPROBACIONES

def imprimeEjes(E, fil, col):
    for i in range (0,fil):
        for j in range (0, col*fil):
            print(E[i][j], " " , end="")
        print("\n")

#RELLENA EL DICCIONARIO V CON NODOS NO VISITADOS

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

def recorreLista(V, E, fil, col, sal, des, camino, tent):

    #INICIALIZAMOS CON CEROS
    matrizPinta = np.zeros(((fil*2)+1,(col*2)+1))
    for i in range(0,(fil)):
        for j in range(0,(col)):
            
            #METEMOS EN CADA POSICION SU PESO CORRESPONDIENTE
            matrizPinta[i*2+1][j*2+1] = tent[id(i,j,c)]

            #ARRAY QUE NOS VA A SERVIR PARA SABER SI ESA POSICION ESTÁ EN EL ARRAY DE EJES
            array =[]
            for v in range(0, len(E[id(i,j,c)])):
                array.append(E[id(i,j,c)][v].getNodo().compNum())
            if((i<f-1) and id(i+1,j,c) in array):
                matrizPinta[ i*2+2 ][ j*2+1 ] = tent[id(i+1,j,c)]
            
            #REINICIAMOS EL ARRAY PARA LAS SIGUIENTES ITERACIONES
            array =[]
            for v in range(0, len(E[id(i,j,c)])):
                array.append(E[id(i,j,c)][v].getNodo().compNum())
            if((j<c-1) and id(i,j+1,c) in array):
                matrizPinta[ i*2+1 ][ j*2+2 ] = tent[id(i,j+1,c)]
    
    
    
    #BUCLES PARA METER EN CADA PASILLO LA MENOR DISTANCIA DE LOS NODOS QUE CONECTA. PARA SACAR LA POSICION OBTENEMOS LA MEDIA ENTRE ESOS DOS NODOS Y PARA
    #SACAR EL COLOR LO HACEMOS CON UN ARRAY DE COLORES Y LA SENTENCIA NP.MIN
    for i in range(0, len(E)-1):
        for j in range (0, len(E[i])):
            color = []
            color.append(tent[i])
            color.append(tent[E[i][j].getNodo().compNum()])
            minimo = np.min(color)
            matrizPinta[int((((fila(i,col))*2+1)+((fila(E[i][j].getNodo().compNum(),col))*2+1))/2)][int((((columna(i,col))*2+1)+((columna(E[i][j].getNodo().compNum(),col))*2+1))/2)] = minimo

    #PINTAMOS LOS NODOS DEL CAMINO
    for k in range(len(camino)):
        matrizPinta[int((fila(camino[k],c)))*2+1][int((columna(camino[k],c)))*2+1] = 500

    #PINTAMOS LOS PASILLOS
    for m in range(len(camino)-1):
        matrizPinta[int((((fila(camino[m],c))*2+1)+((fila(camino[m+1],c))*2+1))/2)][int((((columna(camino[m],c))*2+1)+((columna(camino[m+1],c))*2+1))/2)] = 500
    
    #PINTAMOS EL PRINCIPIO Y EL FINAL DEL CAMINO DE COLORES DISTINTOS
    matrizPinta[fila(sal.compNum(),c)*2+1][columna(sal.compNum(),c)*2+1] = 130
    matrizPinta[fila(des.compNum(),c)*2+1][columna(des.compNum(),c)*2+1] = 130

    return matrizPinta


#ALGORITMO DIJKSTRA
def dijkstra(V, E, salida, llegada):
    #INICIALIZAMOS DICCIONARIO DE DISTANCIAS, DICCIOANRIO DE PADRES, ARRAY EN EL QUE GUARDAMOS EL CAMINO Y LA COLA IGUAL QUE EL ARRAY DE NODOS
    D = {}
    padre = {}
    comprueba = []
    cola = V

    #INICIALIZAMOS EL ARRAY DE DISTANCIAS CON INFINITO EN CADA POSICION MENOS EN LA DE SALIDA QUE GUARDAMOS UN 0
    for v in cola:
        D[cola[v].compNum()] = 999999
    
    D[salida.compNum()] = 0
    
    #MIENTRAS LA COLA NO ESTE VACIA
    while cola:
        distancia_min = None
        
        #SACAMOS EL NODO DE LA DISTANCIA MINIMA
        for i in cola:
            if distancia_min is None:
                distancia_min = cola[i]

            elif D[cola[i].compNum()] < D[distancia_min.compNum()]:
                distancia_min = cola[i]

        
        options = E[distancia_min.compNum()]
        
        #SI SE HA LLEGADO
        if(distancia_min.compNum() == llegada.compNum()):
                break  

        #RECORREMOS LOS HIJOS DE ESE NODO
        for hijos in options:
            if hijos.getPeso() + D[distancia_min.compNum()] < D[hijos.getNodo().compNum()]:
                D[hijos.getNodo().compNum()] = hijos.getPeso() + D[distancia_min.compNum()]
                padre[hijos.getNodo().compNum()] = distancia_min
                

        #SACAMOS EL NODO DE LA COLA
        cola.pop(distancia_min.compNum())


    #MOMENTO EN EL QUE HACMOS EL BACKTRACKING PARA SACAR EL CAMINO, VAMOS HACIA ATRAS METIENDO LOS NODOS DEL CAMINO EN EL ARRAY DE CAMINOS 
    #HASTA QUE LLEGUEMOS A LA SALIDA
    nodoAct = llegada


    while nodoAct.compNum() != salida.compNum():
        comprueba.insert(0, nodoAct.compNum())
        nodoAct = padre[nodoAct.compNum()]
    comprueba.insert(0, salida.compNum())

    return comprueba,D


def dijkstraCF(V, E, salida, llegada):

    #INICIALIZAMOS DICCIONARIO DE DISTANCIAS, DICCIOANRIO DE PADRES, ARRAY EN EL QUE GUARDAMOS EL CAMINO
    D = {}
    D[salida.compNum()] = 0
    padre = {}
    comprueba = []

    #CREAMOS COLA DE PRIORIDAD Y LA INICIALIZAMOS, CON ESTO NOS AHORRAREMOS EL TIEMPO DE BUSQUEDA DEL MINIMO DE LAS DISTANCIAS
    cola = PriorityQueue()                              

    for v in V:
        if V[v].compNum() != salida.compNum():
            D[V[v].compNum()] = 999999
        cola.put((D[V[v].compNum()], V[v].compNum()))
    

    #MIENTRAS LA COLA NO ESTE VACIA
    while cola:

        #SACAMOS EL NODO DE LA DISTANCIA MINIMA
        distancia_min = cola.get()[1]
        options = E[distancia_min]

        #SI SE HA LLEGADO
        if(distancia_min == llegada.compNum()):
                    break    

        #RECORREMOS LOS HIJOS DE ESE NODO
        for hijos in options:
            if hijos.getPeso() + D[distancia_min] < D[hijos.getNodo().compNum()]:
                D[hijos.getNodo().compNum()] = hijos.getPeso() + D[distancia_min]
                padre[hijos.getNodo().compNum()] = distancia_min
                cola.put((D[hijos.getNodo().compNum()], hijos.getNodo().compNum()))
                
    #MOMENTO EN EL QUE HACMOS EL BACKTRACKING PARA SACAR EL CAMINO, VAMOS HACIA ATRAS METIENDO LOS NODOS DEL CAMINO EN EL ARRAY DE CAMINOS 
    #HASTA QUE LLEGUEMOS A LA SALIDA
    nodoAct = llegada.compNum()

    while nodoAct != salida.compNum():
        comprueba.insert(0, nodoAct)
        nodoAct = padre[nodoAct]
    
    comprueba.insert(0, salida.compNum())


    return comprueba,D

def rellenaLista(E, f, c):
    for i in range(0, f*c+1):
        E.append([])
    return E


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

#INICIALIZACION DE EL ARRAY DE NODOS
V = rellenanodos({}, f, c)

#NODOS SALIDA Y DESTINO
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
#camino, distancias = dijkstra(V, E, salida, destino)
camino, distancias = dijkstraCF(V, E, salida, destino)
timedes = time.time()
#FIN DEL DIJKSTRA

#SUSTITUIMOS TODOS LOS INFINITO POR -1 PARA QUE LO PINTE EN EL SET_UNDER DE VERDE
for i in distancias:
    if(distancias[i] == 999999):
        distancias[i] = -1
matrizpinta = recorreLista(V, E, f, c, salida, destino, camino, distancias)
    
#SACAMOS EL COSTE TOTAL Y LO IMORIMIMOS
print("coste: ", distancias[destino.compNum()])


#CALCULO DEL TIEMPO
timeTot = timedes - timeIn
print("\nTiempo de algoritmo: ", timeTot)

cmap=copy.copy(plt.get_cmap("cubehelix"))
cmap.set_under("#FDFF5A")


#Dibujar laberinto
sb.heatmap(matrizpinta,vmin=0,cmap=cmap,cbar_kws={'extend': 'min', 'extendrect': True}, annot=None, fmt="")
plt.show()

plt.colorbar()
plt.show()