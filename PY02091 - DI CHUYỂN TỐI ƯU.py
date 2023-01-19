from collections import deque

for t in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    n = int(input())
    point = set()
    for i in range(n):
        x, y1, y2 = map(int, input().split())
        for y in range(y1, y2+1):
            point.add((x, y))
    if not (sx, sy) in point or not (ex, ey) in point:
        print(-1)
    else:
        ok = False
        Q = deque([(sx, sy, 0)])
        point.remove((sx, sy))
        while len(Q) > 0:
            ux, uy, step = Q.popleft()
            if ux == ex and uy == ey:
                ok = True
                print(step)
                break
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    ox, oy = ux + dx, uy + dy
                    if (ox, oy) in point:
                        point.remove((ox, oy))
                        Q.append((ox, oy, step + 1))
        if not ok: 
            print(-1)
