import math

"""def CheckFermat(primes):
    for i in range(6):
        currentFermat = 2 ** (2 ** i)
        print(f"current fermat number: {currentFermat} ", end="")
        for i in range(3, int(math.sqrt(currentFermat)), 2): 
            if primes[i] > math.sqrt(currentFermat):
                print("is a prime")
                break

            elif currentFermat % primes[i] == 0:
                print(f"is not a prime, divided by {primes[i]}")
                break"""


def GetPrimes(maxNumber):
    primes = []
    primes.append(2)
    primes.append(3)
    for f in range(7):
        fermat = pow(2, pow(2, f)) + 1
        nextPrime = 3
        print(f"{fermat} ", end="")
        while nextPrime < math.sqrt(fermat):
            while True:            
                isPrime = True
                nextPrime += 2
                for i in range(3, int(math.sqrt(nextPrime)), 2):
            
                    if nextPrime % i == 0:
                        isPrime = False
                        break
            
                if isPrime:
                    break
                
                else:
                    nextPrime += 2
            
            #print(nextPrime)
            if not CheckIfPrime(nextPrime, fermat):
                break
            primes.append(nextPrime)
        print()
def CheckIfPrime(prime, fermat):
    if fermat % prime == 0:
        print(f"- is dividable by {prime}", end="")
        return False
    #print(f"{fermat} is not dividable by {prime}")
    return True


primes = GetPrimes(2 ** 64)
print("finished")
#CheckFermat(primes)








