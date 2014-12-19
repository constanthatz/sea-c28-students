def intsum(start=0, stop=100):
    i = start
    j = start
    while i < stop:
        yield j
        i += 1
        j += i
