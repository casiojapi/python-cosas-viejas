#sistema complejo -> muchos elementos, interactuan entre si.

import random
import matplotlib.pyplot as plt
import numpy as np


def generar_bosque(n):
    lista = np.arange(n)
    i=0
    while i < n:
        if lista[i] != 0:
            lista[i] = 0
        i = i+1
    return lista

brazil = generar_bosque(100)

def suceso_aleatorio(prob):
    buleano = False
    if random.random() < prob:
        buleano = True
    return buleano   

def brotes(bosque,p):
    i = 0
    while i < len(bosque):
        if suceso_aleatorio(p):
            bosque[i] = 1
        i=i+1
    return None

def cuantos(bosque, tipo_celda):
    i=0
    lista = 0
    while i < len(bosque):
        if bosque[i] == tipo_celda:
            lista = lista + 1
        i = i+1
    return lista

def rayos(bosque, f):
    i=0
    while i < len(bosque):
        if suceso_aleatorio(f):
            bosque[i] = abs(bosque[i]) * -1
        i=i+1
    return None

def propagacion(bosque):
    
    for k in range (0,len(bosque),1):
        i=0
        while i < len(bosque)-1:
            if bosque[i] == -1:
                bosque[i-1] = abs(bosque[i-1]) * -1 
                bosque[i+1] = abs(bosque[i+1]) * -1
            i=i+1
    return None



def limpieza(bosque):
    i=0
    while i < len(bosque):
        if bosque[i] == -1:
            bosque[i] = 0
        i=i+1
    return None




def incendio_forestal(bosque,p,f,n_rep):

    contador = 0
    for l in range (0, n_rep,1):
        #print(l)
        brotes(bosque,p)
        rayos(bosque,f)
        propagacion(bosque)
        limpieza(bosque)
        i=0
        while i < len(bosque):
            if bosque[i] == 1:
                contador = contador + 1
            i=i+1
    contador = contador / n_rep
    return contador 
        
lista = []

for i in range (0,10,1):
    print(i)
    resultado = incendio_forestal(brazil,i*0.1,.2,100)
    lista.append(resultado)
    


plt.plot(lista, ".")

            
        
        