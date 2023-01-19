T = int(input())
e = []
while True:
    try: e.extend(map(int, input().split()))
    except: break
I = 0
for t in range(T):
    n, m = e[I], e[I+1]
    I+=2
    a = []
    for i in range(n): a.append([0]*m)
    while len(e) - I < n*m: e.append(0)
    for i in range(n):
        for j in range(m): a[i][j] = e[I+j]
        I+=m
    b = []
    for i in range(m):
        b.append([])
        for j in range(n): b[i].append(a[j][i])
    ans = []
    for i in range(n):
        r = []
        for j in range(n):
            x = 0
            for k in range(m): x += a[i][k] * b[k][j]
            r.append(str(x))
        ans.append(r)
    for i in ans: print(' '.join(i))
