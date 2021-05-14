# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random

def generarAlbum(n):
    lista = np.arange(n)
    i=0
    while i < n:
        if lista[i] != 0:
            lista[i] = 0
        i = i+1
    return lista

   

lista1 = generarAlbum(10)
print(lista1)


def comprar(lis):
    m = random.randint(0,len(lis)-1)
    lis[m] = 1
   
comprar(lista1)
print(lista1)