# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:31:56 2015

@author: Dejan
"""
#Pronalazi prvih L prostih brojeva.
#Metod je modifikovano Eratostenovo sito
#Modifikacija se sastoji u tome što je izbjegnuto precrtavanje onih brojeva
#   koji su već precrtani.


from math import *
import numpy as np
import matplotlib.pyplot as plt

print ('How many primes?')
L=int(input())
N=ceil(float(L)*(log(float(L))+log(log(float(L))))) #PNT; N-broj brojeva u kojima se nalazi najmanje L Pn-ova
print (N)
SoE=np.array(range(1,N+2)) #Inicijalizacija sita
#print(len(SoE))
Pn=np.zeros(L,dtype=int)
Pn[0]=2
SoE[1::Pn[0]]=False
ratio=np.zeros(L)
for i in range(1,L):
#    print(i)
    Pn[i]=next(item for item in SoE[i::] if item)
#    
#    print(Pn[i])
    idx=np.array(np.flatnonzero(SoE[:N//Pn[i]]))
    SoE[Pn[i]*(idx+1)-1]=False
    ratio[i]=i*log(i)/Pn[i]
    
plt.plot(range(L),ratio)