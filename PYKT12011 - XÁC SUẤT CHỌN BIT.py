from math import gcd


for t in range(int(input())):
    n, k = map(int, input().split())
    s, a = '0'+input(), [0]*(n+1)
    for i in range(1,n+1):
        a[i] = a[i-1] + (1 if s[i]=='1' else 0)
    r = 0
    for i in range(1, n+1):
        if s[i]=='1':
            if i<=k: r+=1+2*(a[i]-1)
            else: r+=1+2*(a[i]-a[i-k-1]-1)
    m = n*n
    if r==0: print('0/1')
    else:
        x=gcd(r,m)
        print(f'{r//x}/{m//x}')
