#!/usr/bin/bash
cd bld
NPROC=$(nproc)
echo "Compiling with $NPROC cores"
time make -j$NPROC
cd ..