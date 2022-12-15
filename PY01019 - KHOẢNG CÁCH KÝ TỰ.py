for t in range(int(input())):
    def ok(s):
        rs=''.join(reversed(s))
        for i in range(1,len(s)):
            if abs(ord(s[i])-ord(s[i-1])) != abs(ord(rs[i])-ord(rs[i-1])): return 'NO'
        return 'YES'
    print(ok(input()))
