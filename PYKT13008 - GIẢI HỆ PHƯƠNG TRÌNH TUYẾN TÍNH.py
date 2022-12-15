def zero(a: list, n):
    for i in range(n):
        if a[i] != 0: return False
    return True
def cmp(a: list):
    cnt = 0
    for i in range(len(a)-1):
        if a[i]!=0: break
        cnt+=1
    return 1
def solve(a, n):
    for i in range(n):
        if zero(a[i], n): return -1
        a.sort(key=cmp)
        if a[i][i] == 0: continue
        x = a[i][i]
        for j in range(i, n+1): a[i][j]/=x
        for j in range(i+1, n):
            y = a[j][i]
            for k in range(i, n+1): a[j][k] -= y*a[i][k]
    ans = [0]*n
    for i in reversed(range(n)):
        s = 0
        for j in range(i+1, n): s += ans[j]*a[i][j]
        ans[i] = (a[i][-1]-s)/a[i][i]
    return ans
        
for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n): a.append(list(map(int, input().split())))
    b = list(map(int, input().split()))
    for i in range(n): a[i].append(b[i])
    ans = solve(a, n)
    if ans == -1: print(-1)
    else:
        for i in ans: print(f'{i:.3f}', end=' ')
        print()
