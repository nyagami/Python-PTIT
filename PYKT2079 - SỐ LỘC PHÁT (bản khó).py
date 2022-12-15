from sys import stdin
def pow(a, b):
    if b == 0: return 1
    if b&1: return pow(a, b-1)*a
    p = pow(a, b>>1)
    return p*p
_ , __ = [0]*1001, [0]*19
for i in range(1, 1001): _[i] = _[i-1] + ((str(i).count('6') + str(i).count('8')) if i % 8 == 0 else 0)
total = _[-1]
__[1] = _[9]
__[2] = _[99]
__[3] = _[999]
for i in range(4, 19):
    __[i] = __[i-1] * 10 + 2 * pow(10, i - 4) * 125
for t in range(int(stdin.readline())):
    N = int(stdin.readline())
    ans = 0
    if N<=1000: ans = _[N]
    else: 
        n = str(N)
        M = len(n)
        ans += __[M-1]
        pre = 0 
        for i in range(M-3):
            const = pow(10, M-i-4)*125
            x = int(n[i])
            ans += x*__[M-i-1] 
            if i == 0: ans -= __[M-i-1]
            ans += pre*x*const
            if x>6: ans += const
            if x>8: ans += const
            if x==6 or x==8: pre += 1
        last = N%1000
        ans += _[last]
        ans += pre*(1+last//8)
    print(ans)
