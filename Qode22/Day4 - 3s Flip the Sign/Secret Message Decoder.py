import sys
import os

messageFile = "message.txt"
realString = ''
testString = '15836633945'

#OPEN AND READ THE MESSAGE FILE DISCARDING THE CARRAGE RETURNS AND STORE IN A STRING
with open(os.path.join(sys.path[0], messageFile), "r") as f:
    #print(f.read())    #print the file that was loaded to check that it all loads properly
    Lines = f.readlines()
    for line in Lines:
        line = line.strip()
        realString += line
    f.close()

print (realString)

def decodeString(str) -> int:
    addsub = 1
    result = 0
    for char in str:
        if char == '3':
            addsub *= -1
        else:
            result += int(char)*addsub
    return result

print("My Test Result = ", decodeString(testString))
print("My Real Result = ", str(decodeString(realString)))
