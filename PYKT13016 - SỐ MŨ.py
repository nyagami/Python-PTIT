import math


def solve(a : int, b : int, m : int):
    a %= m
    b %= m
    n = int(math.sqrt(m) + 1)

    an = 1
    for i in range(n):
        an = (an * a) % m
    
    vals = {}

    q = 0
    curr = b
    while q <= n:
        vals[curr] = q
        curr = (curr * a) % m
        q += 1
    
    p = 1
    curr = 1
    while p <= n:
        curr = (curr * an) % m
        if curr in vals:
            ans = n * p - vals[curr]
            return ans
        p += 1
    
    return -1

N = int(input())

while N > 0:
    N -= 1
    a, b, m = list(map(int, input().split()))

    print(solve(a, b, m))
