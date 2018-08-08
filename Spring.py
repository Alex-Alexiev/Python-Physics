import matplotlib.pyplot as plt

h = 0
g = 9.8
v = 0

m = 2
k = 19.6
T = 1000

plt.ylabel("Height")

for t in range(0,T):
    Fg = m*g
    Fs = -k*h
    a = (m*(Fg + Fs))/1000
    v += a
    h += v
    if t%10 == 0:
        #print(a,v,h)
        plt.plot(t/1000, h, marker="h", markersize=1, color="blue")

plt.show()
