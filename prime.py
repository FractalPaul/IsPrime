###############################
# is a given number prime
###############################
import sys
import math

# number to check if prime.
num = 2333

# check for any command line arguments
parmLen = len(sys.argv)
if parmLen > 1:
    canidate = sys.argv[1]
    try:
        num = int(canidate)
    except: 
        # do nothing continue on.  bad input. not a number
        print('Number not valid:', canidate)

#######################################################
# given a number check to see if it is prime.
# return True if Prime otherwise False for Composite.
#######################################################
def isPrime(num):
    isPrime = True
    if num==2 or num==3:
        return isPrime
    if num <=1:
        return False
    factor = int(num/2)
    for factors in range(2, factor):
        if num % factors == 0:
            # is not prime
            isPrime = False
            break        
    return isPrime

isp = isPrime(num)
primeLabel = 'Prime' if isp else 'Composite'
print(num, 'is', primeLabel)