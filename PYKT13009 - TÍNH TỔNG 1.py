mod = 1000000007
def power(a, b):
    if b==0: return 1
    if b&1: return power(a, b-1)*a%mod
    p = power(a, b>>1)
    return p*p%mod
def inv(i): return power(i, mod-2)
def solve(n, k):
    G, t = [0]*(k+1), 1
    for i in range(k+1):
        t = t*(n+i)%mod
        G[i] = t*inv(i+1)%mod
    F, f = [0], [n, G[1]]
    for i in range(2, k+1):
        s, r = f[i-1], 0
        new_F = [0 for j in range(i)]
        for j in range(1, i):
            s = (s + F[j-1])%mod
            r = (r + j*s)%mod
            new_F[j] = j*s%mod
        f.append((G[i] - r + mod)%mod)
        F = [new_F[j] for j in range(i)]
    print(f[k])
for t in range(int(input())):
    n, k = map(int, input().split())
    solve(n, k)
