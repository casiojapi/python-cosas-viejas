# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:12:44 2020

@author: maxim
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def crear_tablero(filas, columnas):
    tablero = np.repeat(' ', (filas+2)*(columnas+2)).reshape((filas+2),(columnas+2)) 
    i=0
    while i < filas+2:
        tablero[(i,0)] = "m"
        tablero[(i,columnas+1)] = "m"
        i=i+1
    i=0
    while i < columnas+2:
        tablero[(filas+1,i)] = "m"
        tablero[(0,i)] = "m"
        i=i+1
    return tablero

t = crear_tablero(3,4)



filas = [1, 2, 2, 3, 1]
columnas = [3 , 1, 3, 1, 1]
animal = ["A", "A", "A", "A", "L"]

for i in range (len(animal)):
    t[(filas[i], columnas[i])] = animal[i]
    
print(t)

def es_borde(tablero, coord):
    res = False
    if tablero[coord] == "m":
        res = True
    return res

def vecinos_de(tablero, coord):
    vecinos = []
    if es_borde(tablero, (coord[0]-1, coord[1]-1)) == False:
        vec1 = (coord[0]-1, coord[1]-1)
        vecinos.append(vec1)
    if es_borde(tablero, (coord[0]-1, coord[1])) == False:
        vec2 = (coord[0]-1, coord[1])
        vecinos.append(vec2)
    if es_borde(tablero, (coord[0]-1, coord[1]+1)) == False:
        vec3 = (coord[0]-1, coord[1]+1)
        vecinos.append(vec3)
    if es_borde(tablero, (coord[0], coord[1]+1)) == False:
        vec4 = (coord[0], coord[1]+1)
        vecinos.append(vec4)
    if es_borde(tablero, (coord[0]+1, coord[1]+1)) == False:
        vec5 = (coord[0]+1, coord[1]+1)
        vecinos.append(vec5)
    if es_borde(tablero, (coord[0]+1, coord[1])) == False:
        vec6 = (coord[0]+1, coord[1])
        vecinos.append(vec6)
    if es_borde(tablero, (coord[0]+1, coord[1]-1)) == False:
        vec7 = (coord[0]+1, coord[1]-1)
        vecinos.append(vec7)
    if es_borde(tablero, (coord[0]+1, coord[1]-1)) == False:
        vec8 = (coord[0], coord[1]-1)
        vecinos.append(vec8)
    return vecinos

def buscar_adyacente(tablero, coord, objetivo):
    vec_a = vecinos_de(tablero, coord)
    i=0
    ady = []
    while i < len(vec_a):
        if tablero[(vec_a[i])] == objetivo:
            ady.append(vec_a[i])
            i=len(vec_a)-1
        i=i+1
    ady1 = ady[0]
    return ady1

def mover(tablero, coord):
    if tablero[coord] == 'L':
        vec_b = vecinos_de(tablero, coord)
        i=0
        while i < len(vec_b):
            if tablero[(vec_b[i])] == ' ':
                tablero[coord] = ' '
                tablero[(vec_b[i])] = 'L'
                i=len(vec_b)-1
            i=i+1
    if tablero[coord] == 'A':
        vec_b = vecinos_de(tablero, coord)
        i=0
        while i < len(vec_b):
            if tablero[(vec_b[i])] == ' ':
                tablero[coord] = ' '
                tablero[(vec_b[i])] = 'A'
                i=len(vec_b)-1
            i=i+1
    return None

def alimentar(tablero, coord):
    if tablero[coord] == 'L':
        ant = buscar_adyacente(tablero, coord, 'A')
        if ant != []:
            tablero[coord] = ' '
            tablero[ant] = 'L'
           
alimentar(t,(1,1))
print(t)

def reproducir(tablero, coord):
    if tablero[coord] == 'A':
        amigo = buscar_adyacente(tablero, coord, 'A')
        if amigo != []:
            hijo = buscar_adyacente(tablero, coord, ' ')
            tablero[hijo] = 'A'
    if tablero[coord] == 'L':
        amigo = buscar_adyacente(tablero, coord, 'L')
        if amigo != []:
            hijo = buscar_adyacente(tablero, coord, ' ')
            tablero[hijo] = 'L'
    
def fase_mover(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range (1, cantidad_filas -1):
        for j in range (1, cantidad_columnas -1):
            mover(tablero, (i,j))

def fase_alimentacion(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range (1, cantidad_filas -1):
        for j in range (1, cantidad_columnas -1):
            alimentar(tablero, (i,j))

def fase_reproduccion(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range (1, cantidad_filas -1):
        for j in range (1, cantidad_columnas -1):
            alimentar(tablero, (i,j))
    
def evolucionar(tablero):
    fase_mover(tablero)
    fase_alimentacion(tablero)
    fase_reproduccion(tablero)

def evolucionar_en_el_tiempo(tablero, k):
    for i in range(k):
        evolucionar(tablero)

evolucionar_en_el_tiempo(t,10)
print(t)