import matplotlib.pyplot as plt
import numpy as np

N = 10000
approx = np.zeros(N)

for i in range(0,approx.size):
    approx[i] += ((-1)**i)/((2*i)+1)

pi = np.zeros(N)

for i in range(0,pi.size):
    pi[i] += 4*np.sum(approx[0:i])

plt.plot(pi)
plt.show()

print(pi[-1:])