# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:31:35 2020

@author: maxim
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def crear_tablero(n):
    tablero = np.repeat(0, (n+2)*(n+2)).reshape((n+2),(n+2)) 
    i=0
    while i<len(tablero):
        tablero[(0,i)] = -1
        tablero[(len(tablero)-1,i)] = -1
        tablero[(i,0)] = -1
        tablero[(i,len(tablero)-1)] = -1
        i=i+1
    return tablero

def es_borde(tablero, coord):
    res = False
    if tablero[coord] == -1:
        res = True
    return res


def tirar_copo(tablero, coord):
    if es_borde(tablero,coord) == False:
        tablero[coord] = tablero[coord]+1
    return None


def vecinos_de(tablero, coord):
    vecinos = []
    vec0 = coord[0]+1,coord[1]
    vec1 = coord[0]-1,coord[1]
    vec2 = coord[0],coord[1]+1
    vec3 = coord[0],coord[1]-1

    if es_borde(tablero,vec0) == False:
        vecinos.append(vec0)
    if es_borde(tablero,vec1) == False:
        vecinos.append(vec1)
    if es_borde(tablero,vec2) == False:
        vecinos.append(vec2)
    if es_borde(tablero,vec3) == False:
        vecinos.append(vec3)
    return vecinos


def desbordar_posicion(tablero,coord):
    if tablero[coord] >=4:
        tablero[coord] = 0
        vecinos = vecinos_de(tablero, coord)
        l=0
        while l < len(vecinos):
            tablero[vecinos[l]] = tablero[vecinos[l]] +1
            l = l+1
    return None

def desbordar_arenero(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range (1, cantidad_filas -1):
        for j in range (1, cantidad_columnas -1):
            desbordar_posicion(tablero, (i,j))

def hay_que_desbordar(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    res = False
    for i in range (1, cantidad_filas -1):
        for j in range (1, cantidad_columnas -1):
            if tablero[(i,j)] >=4:
                res = True
    return res

def estabilizar(tablero):
    while (hay_que_desbordar(tablero)):
        desbordar_arenero(tablero)
        
def paso(tablero):
    coord = ((len(tablero)//4)+3*(len(tablero)//4),len(tablero)//4)
    tirar_copo(tablero, coord)
    coord = (len(tablero)//2,len(tablero)//2)
    tirar_copo(tablero, coord)
    estabilizar(tablero)
    
def pasoPija(tablero):
    coord = (8,10)
    tirar_copo(tablero, coord)
    coord1 = (8,20)
    tirar_copo(tablero, coord1)
    estabilizar(tablero)
    coord2 = (12,15)
    tirar_copo(tablero, coord2)
    coord3 = (16,15)
    tirar_copo(tablero, coord3)
    coord4 = (20,15)
    tirar_copo(tablero, coord4)
    coord5 = (22,15)
    tirar_copo(tablero, coord5)
    estabilizar(tablero)
    
    
t1 = crear_tablero(30)
ims = []
fig = plt.figure()
for i in range(80):
    pasoPija(t1)
    im = plt.imshow(t1, animated=True)
    ims.append([im])
ani = animation.ArtistAnimation(fig, ims, interval=50, blit = True,
repeat_delay=400)
print(" Listo para guardar animacion ")
ani.save("dynamic_images_pija.mp4")
plt.show()




#t[(2,3)] = 1 #arranca de 0, acceder a xy valor de array (lo que va entre parentesis se llama *tupla*)