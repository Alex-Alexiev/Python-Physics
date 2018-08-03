import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(['float32(float32,float32)'], target = 'cuda')
def  VectorAdd(a,b):
    return a+b

def main():
    start = timer()
    N = 10000000
    A = np.ones(N, dtype = np.float32)
    B = np.ones(N, dtype = np.float32)
    C = VectorAdd(A,B)
    print(C)
    print(timer()-start)


if __name__ == '__main__':
    main()
