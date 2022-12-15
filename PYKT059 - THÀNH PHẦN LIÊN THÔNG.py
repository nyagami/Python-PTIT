n, m, x = map(int, input().split())
ke = [[] for x in range(0, n+1)]
for i in range(m):
    a, b = map(int, input().split())
    ke[a].append(b)
    ke[b].append(a)
un, q, = [0]*(n+1), [x]
un[x]=1
while len(q)>0:
    u = q.pop()
    for i in ke[u]:
        if un[i]==0:
            q.append(i)
            un[i]=1
check = True
for i in range(1,n+1):
    if un[i]==0:
        check = False
        print(i)
if check: print(0)
