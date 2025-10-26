from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(name="lebwohl_pyx1", ext_modules = cythonize("lebwohl_pyx1.pyx"), include_dirs=[numpy.get_include()])
