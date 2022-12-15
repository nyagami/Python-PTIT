def check(a: list, k, x):
    cnt = 0
    b = a.copy()
    for i in range(1, len(b)):
        if b[i] + b[i-1] < x: continue
        else:
            b[i]+=b[i-1]
            cnt += b[i]//x
            b[i]%=x
    if cnt>=k: return True
    return False
for t in range(int(input())):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    s = 0
    for i in a: s+=i
    p = s//k
    l, r = 0, p
    while l < r:
        mid = (l+r+1)>>1
        if check(a, k, mid): l = mid
        else: r = mid - 1
    print(l*k)
