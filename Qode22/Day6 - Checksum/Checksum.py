import sys
import os

codeFile = "streams.txt"
checksums = []

#OPEN AND READ THE MESSAGE FILE DISCARDING THE CARRAGE RETURNS AND STORE IN A STRING
file = open(os.path.join(sys.path[0], codeFile), "r")

def getChecksum(message) -> int:
    checksum = message[-10:]    #last 10 characters of string
    return (int(checksum))

def getSerialNum(message) -> str:
    return (message[:10])      #first 10 characters of string

def getMartianChecksum(message) -> str:
    return (message[10:-10])      #first 10 characters of string


def getMessageSum(message) -> int:
    sum = 0
    #check if first and last numbers are the same, then circular
    if message[0] == message[-1:]:
        sum += int(message[0])
        
    #check the next digits
    nextnum = 0
    for i, num in enumerate(message):
        if i+1 < len(message):
            currentNum = int(num)
            nextNum = int(message[i+1])
            
            if currentNum == nextNum:
                sum += currentNum
    return sum

lines = file.readlines()
correctSerialNumber = ""

for line in lines:
    line = line.strip() #remove carrage returns
    #print (getMessage(line))
    lineSum = getMessageSum(getMartianChecksum(line))
    checkSum = getChecksum(line)
    isMatch = False
    if lineSum == checkSum:
        isMatch = True
        correctSerialNumber = line
        print("MESSAGE: ", lineSum, " CHECKSUM: ", checkSum, " IS MATCH ", isMatch, " LINE: ", line, " SERIAL: ", getSerialNum(line), "Martian Checksum: ", getMartianChecksum(line))


print ("The correct Serial Number = ", correctSerialNumber)


test = '11517083081221'
print("test case: ", getMessageSum(test))
