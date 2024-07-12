def smallest_multiple(n: int) -> int:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    result = 1
    for num in range(n//2, n+1):
        print(num)
        result = int(result * num / gcd(result, num))
        print(result)
    print("Found the funcker")
    return result % 1_000_000_007


import time

t1 = time.time()
print(smallest_multiple(1000))
t2 = time.time()
print(t2-t1)
