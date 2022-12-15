from math import sqrt

def nt(x):
    if x<2: return False
    if x==2: return True
    if x%2==0: return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x%i==0: return False
    return True
def check(s):
    sum=0
    for i in s:
        if not nt(int(i)): return 'No'
        sum+=int(i)
    if nt(sum) and nt(int(s)) and nt(int(str(''.join(reversed(s))))): return 'Yes'
    return 'No'
for t in range(int(input())):
    print(check(input()))
