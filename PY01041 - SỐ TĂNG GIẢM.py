for t in range(int(input())):
    def ans(n):
        if len(n)<3: return 'NO'
        i=0
        while i<len(n)-1 and n[i]<n[i+1]: i+=1
        while i<len(n)-1 and n[i]>n[i+1]: i+=1
        return 'YES' if i==len(n)-1 else 'NO'
    print(ans(input()))
