import math

def sumdigt(n):
    s=0
    for x in str(n): s+=int(x)
    return s

def prime(n):
    if(n<2): return False
    if(n==2): return True
    if(n%2==0): return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0: return False
    return True

for t in range(int(input())):
    a,b=input().split()
    g=math.gcd(int(a),int(b))
    print('YES') if prime(sumdigt(g)) else print('NO')
