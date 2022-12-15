for t in range(int(input())):
    c=0
    tl=0
    l=1
    s=input()
    for i in range(len(s)):
        if i%2==1: c+=int(s[i])
        else:
            if s[i]=='0': continue
            l*=int(s[i])
            tl=1
    l*=tl
    print(f'{l} {c}')
