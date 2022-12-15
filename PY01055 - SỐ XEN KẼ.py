for t in range(int(input())):
    def check(s):
        if len(s)%2==0: return 'NO'
        for i in range(0,len(s),2):
            if s[i]!=s[0]: return 'NO'
        return 'YES'
    print(check(input()))
