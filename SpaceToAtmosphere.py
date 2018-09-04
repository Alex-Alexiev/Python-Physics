import numpy as np
import matplotlib.pyplot as plt

h = 100000 #initial height m
T = 100000 #fall time ms

p0 = 101.325 #sea level standard atmospheric pressure, 101.325 kPa
t0 = 288.15 #sea level standard temperature, 288.15 K
g = 9.80665 #earth-surface gravitational acceleration, 9.80665 m/s2
L= 0.0065 #temperature lapse rate, 0.0065 Kelvin/m
R = 8.31447 #ideal (universal) gas constant, 8.31447 J/(mol·K)
M = 0.0289644 #molar mass of dry air, 0.0289644 kg/mol

A = 1 #surface area m^2
P = 0 #air density kg/m^3
k = 0.01 #co-efficient of drag
Fd = 0 #(APkv^2)/2

G = 6.67*(10**-11) #universal gravitational constant 
Me = 5.972*(10**24) #mass of earth kg
Mo = 1 #object mass kg
Re = 6.371*(10**6) #radius of earth m

Fg = 0 #GMm/r^2

a = 0
v = 0

plt.ylabel("Velocity")

for t in range(0,T):
    Fg = Mo*g
    Fd = -(A*P*k*(v**2))/2
    a = ((Fg+Fd)/Mo)/1000
    #print("Fg:",Fg, "Fd:",Fd, "a:",a,"v:",v) 
    v+=a
    if t%100 == 0:
        plt.plot(t/1000, v, marker='v', markersize=1, color="blue")

plt.show()

