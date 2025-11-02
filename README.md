## Lebwohl Lasher accelerated python SCIFM0004 Assessment 2

#### Overview

Here, code for simulating the behaviour of liquid crystals in 2D according to the lebwohl lasher model has been accelerated using various means. 

This includes: 
- numba 
- cython
- parallel cython
- numpyvectorisation
- mpi4py.

#### Usage:
```sh 
python program.py <ITERATIONS> <SIZE> <TEMPERATURE> <PLOTFLAG>
```
#### Or, for mpi4py:
```sh
mpiexec --use-hwthread-cpus -n <NUMCORES> python lebwohl_mpi4py.py <ITERATIONS> <SIZE> <TEMPERATURE> <PLOTFLAG> 
```


where:


  **ITERATIONS** = Number of Monte Carlo steps, where 1MCS is when each cell has attempted a change once on average (i.e. SIZE*SIZE attempts)

  **SIZE** = Side length of square lattice

  **TEMPERATURE** = Reduced temperature in range 0.0 - 2.0.

  **PLOTFLAG** = 0 for no plot, 1 for energy plot and 2 for angle plot.

  **NUMCORES** = The desired number of cores (the --use-hwthread-cpus flag also allows the use of hyperthreading / logical processors)

For the parallel cython version, an additional **THREADS** argument is added at the end to specify the desired number of threads.

The original code was written by Dr. Simon Hanna, University of Bristol.
