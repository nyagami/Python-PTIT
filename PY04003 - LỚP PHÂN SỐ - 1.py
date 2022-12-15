from math import gcd
a, b = map(int, input().split())
print(f'{a//gcd(a,b)}/{b//gcd(a,b)}')
