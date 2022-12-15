from math import sqrt
def nt(x):
    if x<2: return False
    if x==2: return True
    if x%2==0: return False
    for i in range(3,int(sqrt(x))+1,2):
        if x%i==0: return False
    return True
a = {}
input()
arr = [int(x) for x in input().split() if nt(int(x))]
for x in arr:
    if a.get(x): a[x]+=1
    else: a[x]=1
for i in a: print(f"{i} {a[i]}")
