for t in range(int(input())):
    def tcs(n):
        s=0
        for i in n: s+=int(i)
        return 'YES' if s%3==0 else 'NO'
    print(tcs(input()))
