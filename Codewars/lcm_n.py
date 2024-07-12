import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes(n):
    # Get the list of primes <= n
    primes = []
    for num in range(n+1):
        if is_prime(num):
            primes.append(num)

    return primes


def smallest_multiple(n: int) -> int:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    result = 1
    for num in range(n//2, n+1):
        print(num)
        result = result * num / gcd(result, num)
        print(result)
    print("Found the funcker")
    return int(result) % 1_000_000_007
