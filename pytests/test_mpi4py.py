import numpy as np
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))

from mpi4py_accel.lebwohl_mpi4py import initdat
def test_initdat_initialization():
    size = 10
    array = initdat(size)
    assert array.shape == (size,size)
    assert np.all(array < 2*np.pi) #Checks initdat works as instructed (This is mainly here as a test pytest)

def test_initdat_differs():
    size = 50
    array1 = initdat(size)
    array2 = initdat(size)
    assert not np.allclose(array1, array2) #Checks that two different dataframes have been made, showing the seed is not fixed

from mpi4py_accel.lebwohl_mpi4py import all_energy
from mpi4py_accel.lebwohl_mpi4py import one_energy
def test_all_energy_calc():
    n = np.random.randint(3, 21)
    arr = np.zeros((n,n))
    arr_energy = all_energy(arr)
    assert arr_energy == n*n*-4
