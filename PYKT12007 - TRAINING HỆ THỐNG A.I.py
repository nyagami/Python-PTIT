for t in range(int(input())):
    n = int(input())
    s = float(input())
    arr = list(map(float, input().split()))
    a = {}
    for i in arr:
        if a.get(i) is None: a[i] = 1
        else: a[i]+=1
    a = [[i, a[i]] for i in sorted(a)]
    while len(a)>1:
        dis = a[1][0]-a[0][0]
        if s>dis*a[0][1]:
            s-=dis*a[0][1]
            a[1][1] += a[0][1]
            a.pop(0)
        else: break
    a[0][0] += s/a[0][1]
    ans = 1
    for i in a:
        ans*=i[0]**i[1]
    print(f'{min(1, ans):.6f}')
