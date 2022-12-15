
from math import gcd


def check(a, l, r, len):
    for i in range(l, r-len+2):
        x = a[i]
        for j in range(i+1, i+len): x = gcd(x, a[j])
        if x==1: return True
    return False

def find_min(a, l, r):
    oke = False
    L, R = 0, r-l+2
    while L < R:
        len = (L+R) >> 1
        if check(a, l, r, len):
            oke = True
            R = len
        else: L = len + 1
    return (oke, L)

def solve(e, I):
    n, k = e[I:I+2]
    I+=2
    a = e[I:I+n]
    I+=n
    if k <= 0: return I
    for i in range(n):
        if a[i] % k == 0:
            a[i]//=k
            if a[i] == 1:
                print(1)
                return I
        else: a[i] = -1
    l, r, ans, oke = 0, 0, 10**9, False
    while l < n and r < n:
        while l < n and a[l] == -1: l+=1
        if l == n: break
        r=l
        while r<n-1 and a[r+1] != -1: r+=1
        res = find_min(a, l, r)
        if res[0] == True:
            oke = True
            ans = min(ans, res[1])
        l = r + 1
    if oke: print(ans)
    else: print(-1)
    return I

T = int(input())
e = []
while True:
    try: e.extend(map(int, input().split()))
    except: break
I = 0
for t in range(T): I = solve(e, I)
    
