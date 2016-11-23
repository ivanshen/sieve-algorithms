from time import time
from atkins import atkins
from eraosthenes import eraosthenes
from zakiya import zak
from sundaram import sundaram

if __name__ == "__main__":
    k = int(input("Sieve algorithms.\nEnter an integer greater than 1. \n"))
    assert k > 1, "Enter an integer greater than 1!"
    start = time()
    zak(k)
    end = time()
    print("Sieve of Zakiya: " + str(end - start))
    start = time()
    eraosthenes(k)
    end = time()
    print("Sieve of Eraosthenes: " + str(end - start))
    start = time()
    sundaram(k)
    end = time()
    print("Sieve of Sundaram: " + str(end - start))
    start = time()
    atkins(k)
    end = time()
    print("Sieve of Atkins: " + str(end - start))
