n = int(input())
par = [-1]*(n+1)
def root(x):
    if par[x] < 0: return x
    par[x] = root(par[x])
    return par[x]
def merge(x, y):
    x = root(x)
    y = root(y)
    if x==y: return
    if par[y] < par[x]: 
        tmp = x
        x = y
        y = tmp
    par[x] += par[y]
    par[y] = x
for i in range(n):
    x, y, z = map(int, input().split())
    if z == 1: merge(x, y)
    else: print(1 if root(x) == root(y) else 0)
