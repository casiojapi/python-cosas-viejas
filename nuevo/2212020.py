# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:29:31 2020

@author: gordo puto
"""

import numpy as np
import math
import matplotlib.pyplot as plt

G = 6.693*10**(-11 )
M = 1.98*10**30 
tiempo = []
tiempo = np.arange(20)

#for i in range (0,len(tiempo),1):

x_lista = [-147095000000.0, -147095000000.0]
y_lista = [0.0, 2617920000.0]

pos_0 = [x_lista[0], y_lista[0]]
pos_1 = [x_lista[1], y_lista[1]]
acc_1 = []
dt = 60*60*24
x_sol = [0] 
y_sol = [0]
sol = [x_sol[0], y_sol[0]]
lista_acc_x = []
lista_acc_y = []
dias = [0,1]
tiempo_total = 400

def calcula_delta(x_sol, x_tierra):
    res = abs(x_sol - x_tierra)
    return res

def calcula_distancia(pos_sol, pos_tierra):
    dis_x = calcula_delta(pos_sol[0],pos_tierra[0])
    dis_y = calcula_delta(pos_sol[1],pos_tierra[1])
    distancia = [dis_x, dis_y]
    return distancia


def calcula_aceleracion(pos_sol , pos_tierra):
    distancia = calcula_distancia(pos_sol, pos_tierra)
    dis_x = calcula_delta(pos_sol[0],pos_tierra[0])
    dis_y = calcula_delta(pos_sol[1],pos_tierra[1])
    acc_x = ((G*M)/(distancia**2))*((0-dis_x)/distancia)
    acc_y = ((G*M)/(distancia**2))*((0-dis_y)/distancia)
    acc_grav = [acc_x, acc_y]
    lista_acc_x.append(acc_x)
    lista_acc_y.append(acc_y)
    return acc_grav

def realiza_verlet(pos_anterior,pos_actual,aceleracion_actual,dt):
    print(pos_anterior)
    distancia3 = calcula_distancia(sol,pos_actual)
    pos_post_x = 2*pos_actual[1]-pos_anterior[1]+((G*M)/((distancia3[1])**2))*dt**2
    pos_post_y = 2*pos_actual[1]-pos_anterior[1]+((G*M)/((distancia3[1])**2))*dt**2
    pos_post = [pos_post_x, pos_post_y]
    return pos_post


print(realiza_verlet(pos_0,pos_1,dt))
    

    
    
    

#def sacar(inicio,fin,tiempo_total):
    #dias = np.arange(tiempo_total)
    #i=0
    #for i in range(inicio,fin,1):
       # sol = [x_sol, y_sol]
     #   tierra = [x_lista[i], y_lista[i]]
      #  dt = tiempo[fin] - tiempo[inicio]
        







