s = 0  # the sum
for i in range(1, 1001):
    if (i % 2) == 0:      # is this an even number?
        if ( "4" in str(i) ):
            #print(i)     # sanity check that the numbers all have 4's in them
            s += i        # and let's add it to our sum
print(s)