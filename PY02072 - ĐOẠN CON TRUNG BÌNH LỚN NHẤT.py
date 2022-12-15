n, a= int(input()), list(map(int, input().split()))
m = max(a)
ans, i = 0, 0
while i<n:
    if a[i]==m:
        cnt = 0
        while i<n and a[i]==m:
            i+=1
            cnt+=1
        ans = max(ans, cnt)
    else: i+=1
print(ans)
