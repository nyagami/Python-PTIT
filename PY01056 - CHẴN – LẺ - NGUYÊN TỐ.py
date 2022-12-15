import math


for t in range(int(input())):
    def nt(n):
        if n<2: return False
        if n==2: return True
        if n%2==0: return False
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i==0: return False
        return True
    def check(s):
        sum=0
        for i in range(len(s)):
            x=int(s[i])
            if (x+i)%2==1: return 'NO'
            sum+=x
        if(nt(sum)): return 'YES'
        return 'NO'
    print(check(input()))
