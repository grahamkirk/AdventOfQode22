import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from MYPYTHONLIBRARY.myfunctions import *

p = 0 # number of primes counted

# Test 1...29 = 10 Primes set second number to 30 to include 29 in range
for n in range(1,1000004):
    if isprime(n):
        p += 1

print("Number of Primes: ", p)