from math import sqrt
n, a = int(input()), list(map(int, input().split()))
b = []
for i in a:
    if b.count(i) == 0: b.append(i)
for i in range(1,len(b)): b[i]+=b[i-1]
def nt(x):
    if x<2: return False
    if x==2: return True
    if x%2==0: return False
    for i in range(3,int(sqrt(x))+1,2):
        if x%i==0: return False
    return True
def find():
    for i in range(len(b) - 1):
        if nt(b[i]) and nt(b[len(b)-1] - b[i]): return i
    return 'NOT FOUND'
print(find())
