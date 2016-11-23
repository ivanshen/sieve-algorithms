import math


def atkins(k):
    nums = {x : False for x in range(5, k + 1)}
    for x in range(1, math.ceil(math.sqrt(k))):
        for y in range(1, math.ceil(math.sqrt(k))):
            n = 4 * x * x + y *y
            if n < k and (n % 12 == 1 or n % 12 == 5):
                nums[n] = not nums[n]
            n = 3 * x * x + y * y
            if n < k and n % 12 == 7:
                nums[n] = not nums[n]
            n = 3 * x * x - y * y
            if x > y and n <= k and n % 12 == 11:
                nums[n] = not nums[n]
    for x in range(5, math.ceil(math.sqrt(k + 1)), 2):
        if nums[x]:
            for y in range(x**2, math.ceil(math.sqrt(k + 1)), x):
                nums[y] = False
    nums[2] = nums[3] = nums[5] = True
    primes = [x for x in nums if nums[x]]
    # print(primes)
