from math import sqrt
def dis(a, b): return sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2))
def area(a, b, c):
    s = sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4
    return s
t = int(input())
l = []
for i in range(t): l.extend([float(x) for x in input().split()])
i = 0
for j in range(t):
    a = dis([l[i], l[i+1]],[l[i+2], l[i+3]])
    b = dis([l[i+2], l[i+3]],[l[i+4], l[i+5]])
    c = dis([l[i+4], l[i+5]], [l[i], l[i+1]])
    i+=6
    if max([a,b,c])*2 >= a+b+c: print('INVALID')
    else: print(f'{area(a, b, c):.2f}')
