import math

######################################################################################
#PRIME CHECK FUNCTION - check to see whether a number is a prime number
######################################################################################
def isprime(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                #print(num, "is not a prime number")
                return False
        else:
            #print(num, "is a prime number")
            return True
    else:
        #print(num, "is not a prime number")
        return False


######################################################################################
#COMBINATION - correct calculation of combinations, n choose k
######################################################################################
def combination(n, r): 
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

######################################################################################
#PASCALS TRIANGLE - build a representation of Pascal's Triangle of a set # of rows
######################################################################################
def pascals_triangle(rows):
    result = [] # need something to collect our results in
    for count in range(rows): # start at 0, up to but not including rows number.
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            row.append(combination(count, element))
        result.append(row)
    return result

######################################################################################
# Number Checkers - Check to see if a number meets certain criteria
######################################################################################

#IS EVEN - Check to see if a number is Even
def isEven(num) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False

#IS ODD - Check to see if a number is Odd
def isOdd(num) -> bool:
    return (not isEven(num))

#IS SQUARE - Check to see if a number is a Perfect Square
def isSquare(number: int) -> bool:
    """
    Returns True if the provided number is a
    perfect square (and False otherwise).
    """
    return math.isqrt(number) ** 2 == number

#IS CUBE - Check to see if a number is cubic
def isCube(number: int) -> bool:
    """
    Returns True if the provided number is
    cubic (and False otherwise).
    """
    return round(number ** (1 / 3)) ** 3 == number

######################################################################################
# Fibonacci Number - get the Fibonacci Number at a given index
######################################################################################
def fibonacciNumber(index):
    sequence = []
    i=0
    while i < index:
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i-2] + sequence[i-1])
        i += 1
    return(sequence[index-1])

