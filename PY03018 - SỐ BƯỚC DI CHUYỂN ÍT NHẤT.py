from sys import stdin
from collections import deque

input = stdin.readline
a = [[]]*1000
for t in range(int(input())):
    n, m = map(int, input().split())
    for i in range(n): a[i] = list(map(int, input().split()))
    q = deque()
    ans = [[0]*m for i in range(n)]
    q.append((0,0))
    while len(q):
        i, j = q.popleft()
        if i<n-1:
            d = abs(a[i+1][j] - a[i][j])
            if d and i + d < n and ans[i+d][j] == 0:
                ans[i+d][j] = ans[i][j]+1
                q.append((i+d, j))
        if j<m-1:
            r = abs(a[i][j+1] - a[i][j])
            if r and j + r < m and ans[i][j+r] == 0:
                ans[i][j+r] = ans[i][j]+1
                q.append((i, j+r))
        if i<n-1 and j<m-1:
            dr = abs(a[i+1][j+1] - a[i][j])
            if dr and i+dr<n and j+dr<m and ans[i+dr][j+dr] == 0:
                ans[i+dr][j+dr] = ans[i][j] + 1
                q.append((i+dr, j+dr))
    if ans[n-1][m-1]: print(ans[n-1][m-1])
    else: print(-1)
