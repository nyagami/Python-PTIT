from sys import stdin
#this solution is relative =)), may get TLE 
def solve(i, j, x, y): 
    s, p = i - j, i + j
    a = min(s+y, x) - max(s, 0) + 1
    b = min(p, y) - max(p-x, 0) + 1
    return a*b - 1

for t in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    ans = 0
    X, Y = (x+2)>>1, (y+1)>>1
    for i in range(X):
        for j in range(Y): ans += solve(i, j, x, y) << 1
        if y%2==0: ans += solve(i, y >> 1, x, y)
        if i == (x-1) >> 1: ans <<= 1
    print(ans)
