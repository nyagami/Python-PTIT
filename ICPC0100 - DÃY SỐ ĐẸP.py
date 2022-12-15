for t in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    cnt = 0
    for i in range(n-1):
        m = min(a[i], a[i+1])
        M = max(a[i], a[i+1])
        while m*2<M: 
            cnt+=1
            m*=2
    print(cnt)
