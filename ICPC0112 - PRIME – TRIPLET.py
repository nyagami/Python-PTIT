from math import sqrt
nt, a= [1 for i in range(int(1e6)+2)], []
nt[0]=nt[1]=0
for i in range(2, int(sqrt(1e6))):
    if nt[i]==1:
        for u in range(i, int(1e6/i)): nt[u*i]=0
for i in range(int(1e6)): 
    if nt[i]: a.append(i)
ans = [0 for i in range(int(1e6)+5)]
cnt = 0
for i in range(len(a)-2):
    if a[i+2]-a[i] == 6 and (a[i+1]-a[i] == 2 or a[i+1]-a[i]):
        ans[a[i+2]+1] = cnt + 1
        cnt += 1
for i in range(1, int(1e6)+2):
    if ans[i]>0: continue
    else: ans[i] = ans[i-1]
for t in range(int(input())): print(ans[int(input())])
