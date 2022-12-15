for t in range(int(input())):
    n, m = map(int, input().split())
    a, b = [], []
    for i in range(n): a.append(list(map(int, input().split())))
    for i in range(3): b.append(list(map(int, input().split())))
    s=0
    for i in range(n):
        if i==n-2: break
        for j in range(m):
            if j==m-2: break
            for x in range(3):
                for y in range(3):
                    s+=b[x][y]*a[i+x][j+y]
    print(s)
