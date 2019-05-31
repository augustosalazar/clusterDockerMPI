import sys
from mpi4py import MPI
from utils import primes_counter
import numpy as np
from math import floor
from time import time

comm = MPI.COMM_WORLD
size = comm.size    
rank = comm.rank    

if rank == 0:
	start_time = time() # MPI.Wtime()

conteo = np.zeros(size, dtype=int)

n = int(sys.argv[1])
inf = 10**(n-1)
sup = 10**n-1
m = sup - inf + 1
delta = floor(m/size)
if rank < size - 1:
	a = inf + rank * delta
	b = inf + (rank + 1) * delta - 1
else: # if rank == size - 1 (last process)
	a = inf + rank * delta
	b = sup

primos = np.array(primes_counter(a, b)).astype('int')

comm.Reduce(primos, conteo, root=0)

if rank == 0:
	tiempo = time() - start_time
	print('El numero de primos de %d digitos es %d.\nTiempo: %f' % (n, conteo[0], tiempo))
