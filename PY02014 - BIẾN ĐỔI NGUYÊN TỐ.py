from math import sqrt
N = 110000
nt, NT = [], [1]*N
NT[0]=NT[1]
for i in range(2, int(sqrt(N))+1):
    if NT[i]:
        for j in range(i, N//i): NT[i*j]=0
for i in range(N):
    if NT[i]: nt.append(i)
n, a = int(input()), list(map(int, input().split()))
M = 0
for i in a:
    m = nt[-1]
    for j in nt: m = min(m, abs(j-i))
    M = max(M, m)
print(M)
