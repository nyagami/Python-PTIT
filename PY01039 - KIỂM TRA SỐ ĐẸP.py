for t in range(int(input())):
    def ans(n):
        for i in range(1,len(n)):
            if n[i]==n[i-1] or (i>1 and n[i]!=n[i-2]): return 'NO'
        return 'YES'
    print(ans(input()))
