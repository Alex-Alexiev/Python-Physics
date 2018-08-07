import numpy as np
import matplotlib.pyplot as plt

T = 10000 #ms
A = 1 #m^2
P = 1.225 #kg/m^3
k = 0.01 #co-efficient of drag

m = 1 #kg
g = 9.8 #m/s^2

v = np.zeros(T)
a = np.zeros(T)

for t in range(1,a.size):
    Fg = m*g
    Fd = -(A*P*k*(v[t-1]**2))/2
    a[t] = ((Fg+Fd)/m)/1000
    #print("Fg:",Fg, "Fd:",Fd, "a:",a[t],"v:",v[t])
    v[t] = v[t-1]+a[t]

plt.plot(v)
plt.show()

