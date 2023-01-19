n, m = int(input()), int(input())
zone = []
ke = [[0]*(n+1) for i in range(n+1)]
par = [-1]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    ke[x][y] = ke[y][x] = 1
    p = par[x] if par[y] == -1 else par[y]
    if p == -1:
        zone.append(set([x, y]))
        par[x] = par[y] = len(zone) - 1
    else:
        zone[p].add(x)
        zone[p].add(y)
        par[x] = par[y] = p

def check():
    for z in zone:
        for x in z:
            for y in z:
                if x!=y:
                    if ke[x][y] == 0 or ke[y][x] == 0: return False

    return True
if check(): print('YES')
else: print('NO')
