from mpi4py import MPI
import socket
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('My rank is',rank, ' hostname ',socket.gethostname())
if (rank == 0):
 print ('Soy el primero ')
