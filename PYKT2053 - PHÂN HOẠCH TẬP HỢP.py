from sys import stdin
un, a = [], []
r = [0]
def Try(pre, sum, ind, p, n):
    if sum > p: return
    if ind == 2: 
        r[0] += 1
        return
    if sum == p: return Try(0, 0, ind + 1, p, n)
    for i in range(pre, n):
        if un[i]: 
            un[i] = 0
            Try(i+1, sum+a[i], ind, p, n)
            un[i] = 1
    return

for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    SUM = sum(a)
    if SUM % 3 != 0:
        print(0)
        continue
    un = [1]*n
    r=[0]
    Try(0, 0, 0, SUM//3, n)
    print(r[0])
