from math import sqrt
from sys import stdin
N, mod = 10**6, 10**9+7
U = [0]*(N+1)
for i in range(2, int(sqrt(N))):
    if U[i]==0:
        U[i]=i
        for u in range(i, 1 + N//i): U[i*u]=i
for i in range(int(sqrt(N)), N+1):
    if U[i]==0: U[i]=i
def count(x, n):
    if n<x: return 0
    return n//x + count(x, n//x)
def pow(a, b):
    if b==0: return 1
    if b%2==1: return a*pow(a,b-1)%mod
    p = pow(a,b//2)
    return p*p%mod
for t in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    ans = 1
    for i in range(2, b//2+1):
        if U[i]==i: ans = ans*((count(i, b) - count(i, a-1))*2+1)%mod
    m = 0
    for i in range(b//2+1, b+1):
        if U[i]==i: m+=1
    ans = ans*pow(3,m)%mod
    print(ans)
