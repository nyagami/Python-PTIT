for t in range(int(input())):
    n, cnt= int(input()), 0
    a = sorted([int(x) for x in input().split()])
    for i in range(n):
        l, r = i+1, n-1
        while l < r:
            s = a[l] + a[i] + a[r]
            if s == 0: 
                cnt += 1
                l += 1
            elif s > 0: r -= 1
            else: l += 1
    print(cnt)
