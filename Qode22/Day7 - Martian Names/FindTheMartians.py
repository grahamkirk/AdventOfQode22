import sys
import os

messageFile = "20000Names.txt"
testNames = ['Stephanie Flores', 'Mark Phillips', 'Jason Marshall', 'Elon Musk']
names = []
martianCount = 0

#OPEN AND READ THE FILE DISCARDING THE CARRAGE RETURNS AND STORE IN A STRING
with open(os.path.join(sys.path[0], messageFile), "r") as f:
    #print(f.read())    #print the file that was loaded to check that it all loads properly
    Names = f.readlines()
    for name in Names:
        name = name.strip()
        names.append(name)
    f.close()

def isMARS(name) -> bool:
    isMARS = False
    m = name.lower().count('m')
    a = name.lower().count('a')
    r = name.lower().count('r')
    s = name.lower().count('s')
    if (m==1 and a==1 and r==1 and s==1):
        isMARS = True
    return isMARS

def isMartian(name) -> bool:
    isMartian = False
    
    if isMARS(name):
        m = name.lower().index('m')
        a = name.lower().index('a')
        r = name.lower().index('r')
        s = name.lower().index('s')
        
        if (m < a < r < s):
            isMartian = True
    return isMartian

#print(isMartian(testNames[0]))


for name in names:
    martian = isMartian(name)
#    print("IS MARTIAN: ", name, " - ", martian )
    if martian:
        martianCount += 1
        print("IS MARTIAN: ", name, " - ", martian )
 
print ("Total # of Martians: ", martianCount)            