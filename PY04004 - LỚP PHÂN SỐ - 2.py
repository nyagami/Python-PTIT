from math import gcd
a, b, c, d = map(int, input().split())
a = a*d + b*c
b*=d
print(f'{a//gcd(a,b)}/{b//gcd(a,b)}')
