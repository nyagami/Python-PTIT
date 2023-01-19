from sys import stdin
def main():
    mod = 10**9 + 7

    _all = map(str, stdin.read().split())
    m, d, a, b =  int(next(_all)), int(next(_all)), next(_all), next(_all)
    n = len(a)
    if n * m > 2000000:
        print(0)
        return
    n_2, c, re = n % 2, 1, [0]*n
    list_not_d = list(range(0, d)) + list(range(d+1, 10))
    for i in range(n):
        re[i] = c
        c = c * 10 % m
    dp = [[0]*m for i in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        x, y, r = dp[i-1], dp[i], re[i-1]
        if n_2 ^ i & 1:
            diff = (r * d) % m
            rev = diff - m
            for j in range(m-diff):
                y[j] = (y[j] + x[j + diff]) % mod
            for j in range(m-diff, m):
                y[j] = (y[j] + x[j + rev]) % mod
        else:
            for dd in list_not_d:
                diff = (r * dd)%m
                rev = diff - m
                for j in range(m-diff):
                    y[j] = (y[j] + x[j + diff]) % mod
                for j in range(m-diff, m): 
                    y[j] = (y[j] + x[j + rev]) % mod
    a = str(int(a) - 1).zfill(n)
    def get(s):
        n  = len(s)
        sum = 0 
        ans = 0 
        bad = False
        for i in range(n):
            ptr = n-i-1
            for j in range(int(s[i])):
                if (i % 2) ^ (j == d): continue
                ans += dp[ptr][(sum + j * re[ptr]) % m]
            sum = (sum + int(s[i]) * re[ptr]) % m
            if (i % 2) ^ (int(s[i]) == d):
                bad = True
                break
        if (not bad and not sum): ans += 1
        return ans
    A = get(a)
    B = get(b)
    print((B-A+mod)%mod)
    
if __name__ == '__main__':
    main()
