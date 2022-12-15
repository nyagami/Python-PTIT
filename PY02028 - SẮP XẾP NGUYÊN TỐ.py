from math import sqrt
n, a = int(input()), list(map(int, input().split()))
def nt(x):
    if x<2: return False
    if x==2: return True
    if x%2==0: return False
    for i in range(3,int(sqrt(x)+1),2):
        if x%i==0: return False
    return True
for i in range(n-1):
    if nt(a[i]):
        for j in range(i+1,n):
            if nt(a[j]) and a[i]>a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
for i in a: print(i, end=' ')
