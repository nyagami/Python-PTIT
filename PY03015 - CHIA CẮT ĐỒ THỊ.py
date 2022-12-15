for t in range(int(input())):
    n, m = map(int, input().split())
    ke = [[] for i in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        ke[x].append(y)
        ke[y].append(x)
    connections = []
    un = [1]*(n+1)
    for i in range(1, n+1):
        if un[i]:
            arr, q, un[i] = [], [i], 0
            while len(q) > 0:
                u = q.pop()
                arr.append(u)
                for j in ke[u]:
                    if un[j]:
                        un[j]=0
                        q.append(j)
                        arr.append(j)
            connections.append(arr)
    def count_connect(i, con):
        un = [1]*(n+1)
        for j in con: un[j] = 1
        un[i], cnt = 0, 0
        for j in con:
            if un[j]:
                cnt+=1
                q, un[j] = [j], 0
                while len(q) > 0:
                    u = q.pop()
                    for k in ke[u]:
                        if un[k]:
                            un[k]=0
                            q.append(k)
        return cnt
    M, ans = 0, 0
    for connection in connections:
        for i in connection:
            cnt = count_connect(i, connection)
            if cnt > M:
                M = cnt
                ans = i
    if M>1: print(ans)
    else: print(0)
