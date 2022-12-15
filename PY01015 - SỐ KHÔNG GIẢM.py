for t in range(int(input())):
    def inc(a):
        for i in range(len(a)-1):
            if a[i]>a[i+1]: return 'NO'
        return 'YES'
    print(inc(input()))
