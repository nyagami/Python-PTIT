from sys import stdin, setrecursionlimit
input = stdin.readline
arr, names = [], set()
n = int(input())

for i in range(n):
    name1, sign, name2 = input().split()
    names.add(name1)
    names.add(name2)
    if sign == '>': arr.append((name1, name2))
    else: arr.append((name2, name1))
a = sorted(names)
N = len(a)

def ind(name):
    l, r = 0, N
    while(l<r):
        mid = (l+r)>>1
        if a[mid] == name: return mid
        if a[mid] < name: l=mid+1
        else: r=mid
    return -1

ke = [[] for i in range(N)]
for n1, n2 in arr: ke[ind(n1)].append(ind(n2))
vis = [0]*N
setrecursionlimit(10**6)
def dfs(i):
    vis[i] = 1
    for j in ke[i]:
        if vis[j] == 0: 
            if(dfs(j)): return True
        if vis[j] == 1: return True
    vis[i] = 2
    return False
    
cyc = False
for i in range(N):
    if vis[i] == 0:
        if(dfs(i)):
            cyc = True
            break

if cyc: print('impossible')
else: print('possible')
