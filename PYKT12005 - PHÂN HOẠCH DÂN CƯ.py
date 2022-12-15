for t in range(int(input())):
    n, c, d = map(int, input().split())
    c, d = sorted([c, d])
    a = sorted(map(int, input().split()), reverse=True)
    s1, s2 = 0, 0
    for i in a[:c]: s1+=i
    for i in a[c:c+d]: s2+=i
    print(f'{(s1/c+s2/d):.6f}')
