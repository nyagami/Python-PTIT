mod = 1000000007
n, m, k = map(int, input().split())
row = {}
col = {}
ans=0 
for i in range(k):
    c, x, y = input().split()
    x = int(x)
    y = int(y)
    if c=='R': 
        if row.get(x) is None: row[x]=y
        else:
            row[x]*=y
            row[x]%=mod
    else: 
        if col.get(x) is None: col[x]=y
        else:
            col[x]*=y
            col[x]%=mod
def sumr(x):
    return (m*x+m*(x-1)+1)*m//2%mod
def sumc(x):
    return (n*x + m*((n-1)*n//2))%mod
ans = 0
ans = (n*m+1)*n*m//2%mod
for i in row: 
    ans+=sumr(i)*(row[i]-1)
    ans%=mod
for i in col: 
    ans+=sumc(i)*(col[i]-1)
    ans%-mod
for i in row:
    for j in col:
        x = (i-1)*m + j
        ans = (ans - x*(row[i]+col[j]-1) + x*row[i]*col[j])%mod
ans = (ans+mod)%mod
print(ans)
