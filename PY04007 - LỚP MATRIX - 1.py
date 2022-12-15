for t in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n): a.append(list(map(int, input().split())))
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
