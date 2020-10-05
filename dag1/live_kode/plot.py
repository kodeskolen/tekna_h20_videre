# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:15:55 2020

@author: Marie
"""

# Vi ønsker å plotte funksjonen
# x^2 - 2x + 5
# for x fra 0 til 20
from pylab import arange, plot, show, zeros

def f(x):
    return x**2 - 2*x + 5

x_verdier = arange(0, 20.5, 0.5)
y_verdier = f(x_verdier)
plot(x_verdier, y_verdier)
show()

for x, y in zip(x_verdier, y_verdier):
    print(f"{x} {y}")


print(x_verdier[1])

for indeks in range(10):
    print(x_verdier[indeks])
    
antall_timer = 10
bakteriemengde = zeros(antall_timer)
vekstfaktor = 1.3

bakteriemengde[0] = 2

for time in range(antall_timer-1):
    bakteriemengde[time+1] = bakteriemengde[time]*vekstfaktor
    
print(bakteriemengde)







