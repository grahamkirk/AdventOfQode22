import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from MYPYTHONLIBRARY.myfunctions import *

oddballs = []
i = 1

# create an array of ODD ODD numbers
for number in range (1, 1000):
    if isOdd(number):
        if isOdd(i):
            #print ("is Odd Odd: ", number)
            oddballs.append(number)
        i+=1
            
# find the SUM of oddballs
mySum = 0
for number in oddballs:
    mySum += number

print("TOTAL = ", mySum)