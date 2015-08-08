from __future__ import print_function

from distutils.core import setup
from distutils.extension import Extension

setup(
    author = 'David Vine Argonne National Laboratory',
    description = 'Write data exchange files.',
    py_modules = ['dxtomo'],
    name = 'dxfile',
    requires = (
        'python',
        'h5py',
        ),
    version = '1.4',
)
