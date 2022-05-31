import math

def GetPrimes(ammount):
    primes = []
    primes.append(2)
    primes.append(3)
    
    while len(primes) < ammount:
        nextPrime = primes[len(primes) - 1] + 2

        while True:
            isPrime = True
            for i in range(3, int(math.sqrt(nextPrime)), 2):
                if nextPrime % i == 0:
                    isPrime = False
                    break
            
            if isPrime:
                break
            else:
                nextPrime += 2
        print(len(primes))
        primes.append(nextPrime)

    return primes