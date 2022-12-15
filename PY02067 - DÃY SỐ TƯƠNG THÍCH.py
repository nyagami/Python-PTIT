def f(x, z):
    ok = False
    l, r = 1, x
    while l<r:
        mid = (l + r) >> 1
        if x//mid > z: l = mid + 1
        elif x//mid < z: r = mid - 1
        else: 
            ok = True
            r = mid
    if x//r == z: ok = True
    return (ok, r)
    
def check(a, z):
    s = 0
    for i in a:
        x = f(i, z)
        if x[0] == False: return(False, s)
        s += x[1]
    return (True, s)
n, a = int(input()), list(map(int, input().split()))
m = min(a)
for i in range(m, 0, -1):
    x = check(a, i)
    if x[0]:
        print(x[1])
        break
