from math import sqrt


n,m = [int(x) for x in input().split()]
def nt(x):
    if x<2: return 0
    if x==2: return 1
    if x%2==0: return 0
    for i in range(3,int(sqrt(x))+1):
        if x%i==0: return 0
    return 1
for i in range(n):
    for x in input().split(): print(nt(int(x)),end=' ')
    print('')
