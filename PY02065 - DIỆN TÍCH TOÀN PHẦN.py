def area(h):
    if h==0: return 0
    return h*4+2
for t in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    arr = []
    def inter(i, j, h):
        if i==0 and j==0: return 0
        if i==0: return min(h,arr[i][j-1])
        if j==0: return min(h,arr[i-1][j])
        return min(h,arr[i][j-1]) + min(h,arr[i-1][j])
    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
        for j in range(m):
            s = inter(i, j, a[j])
            ans+=area(a[j])-s*2
    print(ans)
