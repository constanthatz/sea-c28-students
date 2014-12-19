def intsum(start=0, stop=2**100):
    i = start
    j = start
    while i < stop:
        yield j
        i += 1
        j += i


def doubler(start=1, stop=2**100):
    i = start
    while i < stop:
        yield i
        i *= 2
