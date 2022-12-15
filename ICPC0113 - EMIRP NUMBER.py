from math import sqrt
nt, a= [1 for i in range(int(1e6)+10)], []
nt[0]=nt[1]=0
for i in range(2, int(sqrt(1e6))):
    if nt[i]==1:
        for u in range(i, 1000000//i+1): nt[u*i]=0
for i in range(int(1e6)): 
    if nt[i] == 1: a.append(i)
ans=[]
for i in a:
    x=int(''.join(reversed(str(i))))
    if x > i and nt[x]: ans.append([i, x])
for t in range(int(input())):
    n = int(input())
    for i in ans:
        if i[1] < n: print(i[0], i[1], end=' ')
    print()
