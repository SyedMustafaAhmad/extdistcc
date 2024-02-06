import subprocess

def getBenchmark():
    subprocess.run(["./scripts/getsqlite.sh"]) 

def configureBenchmark():
    subprocess.run(["./scripts/configuresqlite.sh"]) 

def runBenchmark():
    subprocess.run(["./scripts/makesqlite.sh"]) 