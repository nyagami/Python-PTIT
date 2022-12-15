def f(x, n):
    ret = 0
    for i in range(0, 10):
        m = 10**i 
        if m > n: break
        a = n // m
        b = n % m
        z = a % 10
        if z > x: ret += ((a // 10) + 1) * m
        elif z == x: ret += (a // 10) * m + (b + 1)
        else: ret += (a // 10) * m
        if x == 0: ret -= m
    return ret
def digitsCount(d, low, high):
    return f(d, high) - f(d, low - 1)

for t in range(int(input())):
    a, b = map(int, input().split())
    for i in range(0, 10): print(digitsCount(i, a, b), end=' ')
    print()
