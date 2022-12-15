for t in range(int(input())):
    s, n = input(), input()
    l1 ,l2 = len(s), len(n)
    cnt = i = 0
    while i<l1:
        if s[i:i+l2] == n:
            cnt+=1
            i+=l2
        else: i+=1
    print(cnt)
