# input = open('d:/code/in.txt').readline
maxn = 33
dp = [[0]*33 for i in range(maxn)]    #dp[i][j] number of number has k bit 0 which has i + 1 bit (first bit = 1) 
for i in range(maxn): dp[i][0] = 1
for i in range(1, maxn):
    for j in range(1, maxn):
        if i<j: dp[i][j] = 0
        else: dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
for t in range(int(input())):
    N, k = map(int, input().split())
    if N == 0:
        print(1 if k == 1 else 0)
        continue
    s = f'{N:b}'
    n = len(s)
    ans, pre = 0, 0
    for i in range(1, n):
        if s[i] == '1' and k > pre: 
            ans += dp[n-i-1][k-pre-1]
        if s[i] == '0': pre += 1
    if pre == k: ans += 1
    for i in range(n-1): ans += dp[i][k]
    if k==1: ans += 1
    print(ans)
