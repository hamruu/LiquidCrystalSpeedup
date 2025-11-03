#Script written to test my slice lattice function works as intended

import sys
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpi4py import MPI

def initdat(nmax):
    return np.random.random_sample((nmax,nmax))*2.0*np.pi

def slice_lattice(nmax, size, rank):
    """
    A helper function designed to decompose the lattice for mpi4py 
    """
    averow = nmax//size
    extra = nmax%size

    if rank < extra:
        rows = averow +1
        start = rank*rows
    else:
        rows = averow
        start = rank*averow + extra
    end = start + rows
    print(f"Mpi rank {rank} is responsible for {rows} rows")
    return start, end, rows

def main(nmax):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        my_lattice = initdat(nmax)

        #slice my_lattice and send a sublattice to each rank
        for r in range(size):
            start, end, rows = slice_lattice(nmax, size, r)
            sublattice = my_lattice[start:end]
            if r == 0:
                #Rank 0 keeps its own sublattice
                local_sublattice = sublattice
            else:
                comm.send(sublattice, dest=r, tag=1)
    else:
        local_sublattice = comm.recv(source=0, tag=1)

    print(f"Rank {rank} received sublattice of shape {local_sublattice.shape}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        nmax = int(sys.argv[1])
        main(nmax)
    else:
        print(f"Usage: python {sys.argv[0]} nmax")

 #MPI.Finalize()