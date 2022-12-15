from math import sqrt
N = 100000
f, nt, a = [], [1]*N, []
nt[0]=nt[1]=0
for i in range(2,int(sqrt(N))):
    if nt[i]==1:
        for u in range(i,N//i): nt[i*u]=0
for i in range(N):
    if nt[i]==1: f.append(i)
N = 10**9 + 7
f.sort()
for i in f:
    if i**8 <= N: a.append(i**8)
    else: break
for i in range(len(f)-1):
    for j in range(i+1,len(f)):
        x = f[i]**2 * f[j]**2
        if x <= N: a.append(x)
        else: break
a.sort()
def up_bow(l, r, x):
    if l==r: return l
    mid = (l+r)//2
    if a[mid] <= x: return up_bow(mid+1, r, x)
    return up_bow(l, mid, x)
print(up_bow(0, len(a)-1, int(input())))
