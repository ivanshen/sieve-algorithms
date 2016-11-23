import math

# SIEVE OF ERAOSTHENES

def eraosthenes(k):
    nums = {x : True for x in range(2, k + 1)}
    p = 2
    for x in range(2, math.ceil(math.sqrt(k + 1))):
        for y in range(p**2, k + 1, p):
            nums[y] = False
        p += 1
    primes = [x for x in nums if nums[x]]
    # print(primes)
