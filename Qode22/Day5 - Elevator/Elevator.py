import sys
import os

codeFile = "codes.txt"
testCode1a = '((' # Blinky Park is located on floor 2
testCode1b = '2(' # Blinky Park is located on floor 2
testCode2a = '(())' # Blinky Park is located on floor 0
testCode2b = '()()' # Blinky Park is located on floor 0
testCode2c = '2(2)' # Blinky Park is located on floor 0
testCode3 = '((())()(())' # Blinky Park is located on floor 1
commands = ''

#OPEN AND READ THE MESSAGE FILE DISCARDING THE CARRAGE RETURNS AND STORE IN A STRING
with open(os.path.join(sys.path[0], codeFile), "r") as codes:
    commands = codes.read()
    print(commands)    #print the file that was loaded to check that it all loads properly
    codes.close()
    
def navigateFloors(commands) -> int:
    floor = 0
    repeat = 1
    for command in commands:
        if command == '(':
            floor += 1 * repeat
            repeat = 1 #reset repeater
        elif command == ')':
            floor -= 1 * repeat
            repeat = 1 #reset repeater
        else:
            repeat = int(command)
    return floor

print("FLOOR: ", navigateFloors(commands))