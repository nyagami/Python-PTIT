inf = 10**18
def solve():
    n, m, k = map(int, input().split())
    c = [0] + list(map(int, input().split()))
    A = int(input())
    x = list(map(int, input().split()))
    x = [i for i in x if i > 0 and i <= n]
    A = len(x)
    B = int(input())
    y = list(map(int, input().split()))
    y = [i for i in y if i > 0 and i <= n]
    B = len(y)

    if m < k or k > n or n < m or k > A or k > B: return print(-1)
    
    I = sorted(set(x).intersection(y),key=lambda x: c[x])
    X = sorted(x, key=lambda x: c[x])
    Y = sorted(y, key=lambda x: c[x])

    #converting code from thanhchaus2
    bool1, bool2 = {}, {}
    for i in I: bool1[i] = True

    take = max(0, 2*k - m)
    if take > len(I): return print(-1)

    total = 0
    for i in range(take):
        if bool2.get(I[i]): continue
        total += c[I[i]]
        bool2[I[i]] = True
        c[I[i]] = -1
        k -= 1
        m -= 1

    x1, x2 = k, k

    for i in range(len(X)):
        if x1 <= 0: break
        if bool2.get(X[i]): continue
        else:    
            total += c[X[i]]
            bool2[X[i]] = True
            if bool1.get(X[i]): x2-=1
            c[X[i]] = -inf
            x1 -= 1
            m -= 1
    for i in range(len(Y)):
        if x2 <= 0: break
        if bool2.get(Y[i]): continue
        else:
            total += c[Y[i]]
            bool2[Y[i]] = True
            c[Y[i]] = -inf
            x2 -= 1
            m -= 1

    if x1 > 0 or x2 > 0: return(print(-1))
    adj = []
    for i in range(1, n+1): adj.append((c[i], i))
    adj.sort()
    for i in range(1, n+1):
        if m <= 0: break
        if bool2.get(adj[i][1]): continue
        total += adj[i][0]
        bool2[adj[i][1]] = True
        m -= 1

    print(-1 if m > 0 else total)

solve()
