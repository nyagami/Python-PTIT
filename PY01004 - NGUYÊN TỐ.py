from math import gcd,sqrt
def isprime(x):
    if x==2: return True
    if x<2: return False
    if x%2==0: return False
    for i in range(3,int(sqrt(x))+1,2):
        if x%i==0: return False
    return True

for ts in range(int(input())):
    n=int(input())
    cnt=0
    for i in range(n):
        if gcd(i,n)==1: cnt+=1
    print('YES') if isprime(cnt) else print('NO')
