#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from setuptools import setup, Extension

setup(
    author = 'David Vine',
    description = 'Write data exchange files.',
    py_modules = ['dxfile'],
    name = 'dxfile',
    requires = (
        'python',
        'h5py',
        ),
    version = '1.5',
)
