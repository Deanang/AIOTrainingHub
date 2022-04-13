def zap(year, a, b):
    while abs(a - b) + 1 != 1:
        year += 1
        a, b = b, abs(a - b) + 1 
    return year + 2

print(zap(2022, 100, 3))