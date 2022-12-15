import math


for t in range(int(input())):
    s=input()
    rs=''.join(reversed(s))
    print('YES') if math.gcd(int(s),int(rs))==1 else print('NO') 
