def intsum(start=0, stop=2**100):
    i, j = start, start
    while i < stop:
        yield j
        i += 1
        j += i


def doubler(start=1, stop=2**100):
    i = start
    while i < stop:
        yield i
        i *= 2


def fib(start=0, stop=2**100):
    i, j = start, start + 1
    while j < stop:
        yield j
        i, j = j, i + j


def prime(start=1, stop=2**100):
    def is_prime(n):
        if n <= 3:
            return n >= 2
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    n = start
    while n < stop:
        if is_prime(n):
            yield n
        n += 1
