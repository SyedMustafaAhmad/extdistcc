import subprocess
import os

def getBenchmark():
    if os.path.exists('sqlite.tar.gz'):
        print('File already exists. Starting configuration ...')
    else:
        subprocess.run(["./scripts/getsqlite.sh"])

def configureBenchmark():
    subprocess.run(["./scripts/configuresqlite.sh"]) 

def runBenchmark():
    subprocess.run(["./scripts/makesqlite.sh"]) 