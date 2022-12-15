from sys import stdin
maxn = 10**6
U = [0]*(maxn + 1)
for i in range(2, 1000):
    if U[i] == 0:
        for u in range(i, 1+maxn//i): U[u*i] = i
for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n < 1:
        print(0)
        continue
    ans = 1
    while(U[n]):
        u = U[n]
        cnt = 0
        while n%u==0:
            cnt+=1
            n//=u
        ans *= (cnt+1)
    if n>1: ans*=2
    print(ans)
