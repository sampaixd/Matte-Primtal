from PrimeCalculator import GetPrimes
import math

def CheckPrimeDifference(primes):
    for i in range(1, len(primes)):
        print(f"difference between prime {primes[i]} and {primes[i - 1]}: {primes[i] - primes[i - 1]}")
        print(f"difference between {i} squared and ({i} + 1) squared: {pow(i + 1, 2) - pow(i, 2)}")


def LegrendeTest(primes):
    correctCount = 0
    incorrectCount = 0
    for x in range(1, int(math.sqrt(primes[-1]))):

        for p in range(len(primes)):
            if primes[p] > pow(x + 1, 2):
                print(f"there is no prime between {pow(x, 2)} and {pow(x + 1, 2)}")
                incorrectCount += 1
                break
            if pow(x + 1, 2) > primes[p] > pow(x, 2):
                print(f"{primes[p]} is a prime between {pow(x, 2)} and {pow(x + 1, 2)}")
                correctCount += 1
                break
    print(f"correct cases: {correctCount}, {correctCount * 100 / (correctCount + incorrectCount)}%")
    print(f"incorrect cases: {incorrectCount}, {incorrectCount * 100 / (correctCount + incorrectCount)}%")

primes = GetPrimes(100000)
print("primes calculated")
#LegrendeTest(primes)
CheckPrimeDifference(primes)

