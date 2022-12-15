from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
def V(a,b,x):
    return x*(a-2*x)*(b-2*x)
def big(a, b):
    arr = []
    for i in range(1,min(a,b)//2):
        arr.append(V(a,b,i))
    arr.sort(reverse=True)
    return arr[:3]
    
for t in range(int(input())):
    a,b,x,y,z,l,r = map(int,input().split())
    v = big(a,b)
    for i in range(x,r+1,v[0]):
        if i%v[1]==y and i%v[2]==z:
            k=i
            break
    if k<l:
        com = lcm(v[0], lcm(v[1], v[2]))
        d = (l-k)//com
        if d*com + k < l: d+=1
        print(d*com+k)
    else: print(k)
