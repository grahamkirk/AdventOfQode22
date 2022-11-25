#PRIME CHECK FUNCTION
def isprime(num):
    if num > 1:
        for n in range(2,num):
            if(num % n) == 0:
                return False
            return True
    else:
        return False