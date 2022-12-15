mod = 1000000007
def power(a, b):
    if b==0: return 1
    if b&1: return power(a, b-1)*a%mod
    p = power(a, b>>1)
    return p*p%mod
def inv(i): return power(i, mod-2)
INV, G = [0]*1002, [0]*1002
for i in range(1,1002): INV[i] = inv(i)
def solve(n, k):
    if k == 0: return n
    T = 1
    for i in range(k+1):
        T = T*(n+i)%mod
        G[i] = T*INV[i+1]%mod
    F, ans = [0], G[1]
    for i in range(2, k+1):
        s, r = ans, 0
        new_F = [0]*i
        for j in range(1, i):
            s = s + F[j-1]
            new_F[j] = j*s%mod
            r = r + new_F[j]
        ans = (G[i] - r + mod)%mod
        F = new_F.copy()
    return ans
for t in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n%mod, k))
