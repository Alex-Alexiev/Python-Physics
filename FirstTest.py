import numpy as np
from timeit import default_timer as timer

def VectorAdd(a,b,c):
        for i in range(a.size):
            c[i]=a[i]+b[i]

def main():
    start = timer()
    N = 10000000
    A = np.ones(N, dtype = np.float32)
    B = np.ones(N, dtype = np.float32)
    C = np.zeros(N, dtype = np.float32)
    VectorAdd(A,B,C)
    print(C)
    print(timer()-start)


if __name__ == '__main__':
    main()
