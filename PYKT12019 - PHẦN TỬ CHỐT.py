e = 10**12
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    arr = [[-1, e] for i in range(n)]
    maxr = e
    for i in range(n-1,-1,-1):
        arr[i][1] = maxr
        maxr = min(maxr, a[i])
    maxl = -1
    for i in range(n):
        arr[i][0] = maxl
        maxl = max(maxl, a[i])
    cnt = 0
    for i in range(n):
        if arr[i][0]<=a[i] and arr[i][1]>a[i]: cnt+=1
    print(cnt)
