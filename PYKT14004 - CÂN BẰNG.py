from sys import stdin
a = list(map(int, stdin.read().split()))
all_sum, n = sum(a), 12
un, s = [1]*12, [0]*4
def Try(g, ind, sum, pre):
    ans = 10**8
    if g == 3:
        s[3] = all_sum - s[0] - s[1] - s[2]
        MAX = max(s)
        MIN = min(s)
        return min(ans, MAX - MIN)
    for i in range(pre, n):
        if un[i]:
            un[i] = 0
            if ind == 2: 
                s[g] = sum + a[i]
                ans = min(ans, Try(g + 1, 0, 0, 0))
            else: ans = min(ans, Try(g, ind + 1, sum + a[i], i + 1))
            un[i] = 1
    return ans
ans = Try(0, 0, 0, 0)
print(ans)
