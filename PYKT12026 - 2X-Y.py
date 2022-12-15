def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)
from sys import stdin

for t in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    g = 0
    for i in range(1,n):
        g = gcd(g, a[i]-a[0])
    if g!= 0 and (k-a[0])%g==0: print('YES')
    else: print('NO')
