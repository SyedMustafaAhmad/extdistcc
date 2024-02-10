#!/usr/bin/bash
rm -rf ./sqlite
rm -rf ./bld
tar xzf sqlite.tar.gz
mkdir bld
cd bld
../sqlite/configure
cd ..