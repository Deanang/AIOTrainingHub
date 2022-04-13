1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonaci(n):
    if n <= 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

def fibonaciDP(n):
    a = b = 1
    for i in range(n-2):
        a, b = b, a+b
    return b

print(fibonaciDP(500307))
#print(fibonaci(35))
