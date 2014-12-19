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
