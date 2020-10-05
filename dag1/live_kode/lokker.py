# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:01:09 2020

@author: Marie
"""

# En petriskål har 2 bakterier. Bakteriene øker med 30% hver time
# Hvor mange batierer er det etter 10 timer?

antall_timer = 10
bakteriemengde = 2
vekstfaktor = 1.3

for time in range(antall_timer):
    bakteriemengde *= vekstfaktor

print(bakteriemengde)



