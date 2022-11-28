import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from MYPYTHONLIBRARY.myfunctions import *

print("is prime: ", isprime(5))

print("fibonacci ", fibonacciNumber(2021))