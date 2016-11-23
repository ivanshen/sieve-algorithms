from time import time
import math

# SIEVE OF SUNDARAM

def sundaram(k):
    nums = {x : True for x in range(1, k + 1)}
    m = int(k // 2)
    for i in range(1, m):
        for j in range(i, math.ceil((m-i)/(2*i+1))):
            nums[i + j + 2*i*j] = False
    primes = [2] + [2 * x + 1 for x in nums if nums[x] and 2 * x + 1 < k + 1]
    # print(primes)
