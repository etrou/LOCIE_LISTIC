# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:55:54 2016

@author: locie
"""


import numpy as np
import matplotlib.pyplot as plt

def mafonction(t, omega = 1., tau = 10.):
    
   
    return np.exp(-t / tau) * np.sin(omega * t) #carré de x (**)

    #[] correspond à une liste 
    
t = np.linspace(0., 10., 1000)
omega = range(10) # valeur de Omega
a = mafonction(t)