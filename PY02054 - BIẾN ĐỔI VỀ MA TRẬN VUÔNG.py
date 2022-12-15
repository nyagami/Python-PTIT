n, m = map(int, input().split())
start = 0 if n>m else (1 if n<m else -1)
wall = start + (abs(n-m)-1)*2
for i in range(n):
    a = input().split()
    if start==0 and i%2==0 and i<=wall: continue
    for j in range(m):
        if start==1 and j%2==1 and j<=wall: continue
        print(a[j], end=' ')
    print('')
