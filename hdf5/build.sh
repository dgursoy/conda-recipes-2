#!/bin/bash

CC=/local/dgursoy/Applications/Anaconda/bin/mpicc ./configure --prefix=$PREFIX --enable-linux-lfs --enable-parallel --enable-shared --with-zlib=$PREFIX --with-ssl
make
make install

rm -rf $PREFIX/share/hdf5_examples