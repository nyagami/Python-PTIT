for t in range(int(input())):
    ans=1
    for i in input():
        if i=='0': continue
        ans*=int(i)
    print(ans)
