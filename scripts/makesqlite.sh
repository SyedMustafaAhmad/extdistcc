#!/usr/bin/bash
cd bld
NPROC=$(nproc)
echo "Compiling with $NPROC cores"
time make clean -j$NPROC
cd ..