from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

ext_modules = [
    Extension(
        "lebwohl_parallel_pyx1",
        ["lebwohl_parallel_pyx1.pyx"],
         extra_compile_args =['-fopenmp','-v','-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include'],
    extra_link_args=['-lgomp', '-Wl,-rpath,/usr/local/opt/gcc/lib/gcc/5/'],
    )
]

setup(name="lebwohl_parallel_pyx1", ext_modules = cythonize(ext_modules), include_dirs=[numpy.get_include()])
