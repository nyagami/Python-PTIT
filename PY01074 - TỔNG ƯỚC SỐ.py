from math import sqrt
from array import array
N, M = 1 + 2*10**6, 2*10**6
U = array('i', [0]*N)
for i in range(2, int(sqrt(M))+1):
    if U[i] == 0:
        U[i] = i
        for u in range(i, M//i+1): U[i*u]=i
del M 
del u
for i in range(4,N): U[i] += U[i//U[i]] if U[i] else i
from sys import stdin
n, s = int(stdin.readline()), 0
while 1:
    try:
        x = int(stdin.readline())
        s += U[x]
    except: break
print(s)
