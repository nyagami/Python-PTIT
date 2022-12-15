import math


for t in range(int(input())):
    def nt(n):
        if n<2: return 'NO'
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0: return 'NO'
        return 'YES'
    print(nt(int(input()[-4:])))
