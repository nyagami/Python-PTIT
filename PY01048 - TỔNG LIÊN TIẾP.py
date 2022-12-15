from math import sqrt
def check(a, b, n):
    return a>0 and b > a and (b+a)*(b-a+1) == n
def U(n):
    a = []
    for i in range(2, int(sqrt(n)) + 1):
        if i*i == n: break
        if n%i==0: a.extend([i, n//i])
    return a
for t in range(int(input())):
    n, ans = int(input())*2, set()
    arr = U(n)
    for i in arr:
        x, y = i, n//i
        b = (x+y-1)//2
        a = x-b
        if check(a, b, n): ans.add((a, b))
    print(len(ans))
