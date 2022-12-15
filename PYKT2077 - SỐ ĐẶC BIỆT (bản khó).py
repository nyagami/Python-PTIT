N = input()
n, d = len(N), [int(i) for i in N]

M = 9*n + 1
NT = [1]*(M)
NT[0], NT[1] = 0, 0
for i in range(3, M):
    for j in range(2, i):
        if i%j == 0: NT[i] = 0
dp = []
for i in range(n):
    dp.append([])
    for carry in range(3): dp[i].append([[0]*M for x in range(M)])

for dx in range(10):
    for dy in range(10):
        dxy = dx + (dy<<1)
        if dxy%10 == d[n-1]: dp[n-1][dxy//10][dx][dy] = 1

for i in reversed(range(1, n)):
    for carry in range(3):
        for x in range((n-i)*9+1):
            for y in range((n-i)*9+1): 
                r = dp[i][carry][x][y]
                if r:
                    for dx in range(10):
                        for dy in range(10):
                            dxy = dx + (dy<<1) + carry
                            if dxy%10 == d[i-1]: dp[i-1][dxy//10][x+dx][y+dy] += r

ans = 0
for i in range(M):
    if not NT[i]: continue
    for j in range(M):
        if NT[j]: ans += dp[0][0][i][j]
print(ans)
