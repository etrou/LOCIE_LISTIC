# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:55:54 2016

@author: locie
"""


import numpy as np
import matplotlib.pyplot as plt

def mafonction(t, omega = 1., tau = 10.):
    print "coucou\n"    
    return np.exp(-t / tau) * np.sin(omega * t) #carré de x (**)

    #[] correspond à une liste 
    
t = np.linspace(0., 10., 1000)
omega = range(10) # valeur de Omega
a = mafonction(t)

plt.figure("Notre figure")
plt.clf() # purge la figure
for i in range (len(omega)):
    color= "bkyrbybybyk"
    line = "- -"
    a=mafonction(t, omega[i])
    plt.plot(t,a, color=color[i], linestyle = line[0], label = "$\omega = {0}$".format(omega[i]))
# plt.plot(t,a, marker = "+", color="m", linewidth=3, linestyle="--")
# plt.plot(t,a, "*c--" linewidth=3) 
plt.legend()
plt.grid()
plt.xlabel("Temps $t$ [s]")
plt.ylabel("Amplitude, $a$, [N]")
plt.show()
plt.savefig("mafigure.pdf")