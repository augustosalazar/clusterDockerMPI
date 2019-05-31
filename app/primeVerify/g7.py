import time
import os
import sys
from mpi4py import MPI



def PList(n,low,cant):
    start = time.time()
    cont=0
    if (n<low) | (n<2) | (low<0): return []
    iLow = low
    low = low//2*2+1
    primes = [1]*((((n+1)//2*2+1)-low)//2)
    raiz = int(n**0.5)+1
    dim = int(len(primes))
    m = 3
    while m < raiz:
        i = (m*m-low)//2
        if i<0: i += m*int((0-i)//m)
        if i<0: i += m
        primes[i:n+1:m] = [0]*((((dim-1)-i)//m)+1)   
        m += 2
    
    primes = [low+(x*2) for x in range(dim) if primes[x]]
   
    if (iLow == 1)|(iLow==0):
        primes[0]=2
    if iLow == 2:
        primes = [2]+primes
        dim = len(primes)-1
    for index in range(0,len(primes)):
      cont=cont+1
    stop = time.time()
    delay = stop-start        
    print('el numero de primos de, ',cant,' digitos es ' ,cont,' tiempo ',delay)

#PRINCIPAL------------------------------------
comm = MPI.COMM_WORLD
nn = comm.Get_size()
rank = comm.Get_rank()
if (rank==0):
    
    m=sys.argv[1]
    print('Longitud de primos: ',m)
    inicial=''
    fin=''
    dig=int(m)
    i=0
    while(i<dig):
      if(i==0):
        inicial='1'
        fin='9'
      else:
        inicial= inicial+'0'
        fin=fin+'9'
      i=i+1  
    low = int(inicial)
    n = int(fin)
    PList(n,low,dig)