n, a, s = int(input()), [], 0
for i in range(n):
    arr = list(map(int, input().split()))
    s+=sum(arr)
    a.append(arr)
if n==2:
    print(1, s//2-1)
else:
    x1 = (sum(a[0]) - s//((n-1)*2))//(n-2)
    print(x1, end=' ')
    for i in range(1,n): print(a[0][i] - x1, end=' ')
