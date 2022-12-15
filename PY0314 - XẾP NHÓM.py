from sys import stdin
# stdin = open('D:/code/in.txt')    
n, k, tmp, a, b = 0, 0, 0, [], []
def check(g):
    l, r = 0, n
    while l<r:
        mid = (l+r)>>1
        if a[mid]<g: l = mid + 1
        else: r = mid
    return b[l-1] >= g*(l+tmp)
for t in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    a = sorted(map(int, stdin.readline().split()))
    b = a.copy()
    for i in range(1, n): b[i]+=b[i-1]
    if n<k:
        print(0)
        continue
    if n==k:
        print(a[0])
        continue
    tmp = k-n
    l, r = 0, sum(a)//k
    while l<r:
        mid = (l+r)>>1
        if check(mid): l = mid + 1
        else: r = mid
    if check(l): print(l)
    else: print(l-1)
