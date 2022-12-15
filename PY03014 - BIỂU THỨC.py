for i in range(int(input())):
    a, s = [], input()
    cnt = 1
    for i in s:
        if i=='(':
            a.append((i, cnt))
            print(cnt, end=' ')
            cnt+=1
        elif i==')':
            print(a[-1][1], end=' ')
            a.pop()
    print()
