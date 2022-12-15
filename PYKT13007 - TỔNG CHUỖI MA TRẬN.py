n, k = map(int, input().split())

z = [[0]*n for i in range(n)]

def add(x, y):
    r = [i.copy() for i in z]
    for i in range(n):
        for j in range(n):
            r[i][j] = (x[i][j] + y[i][j])%10
    return r

def mul(x, y):
    r = [i.copy() for i in z]
    for i in range(n):
        for j in range(n):
            for k in range(n): r[i][j] += x[i][k]*y[k][j]
            r[i][j]%=10
    return r

I = [[0]*n for i in range(n)]

for i in range(n): I[i][i] = 1

def pow(A, B):
    if B==0: return I
    if B&1: return mul(A, pow(A, B-1))
    p = pow(A, B>>1)
    return mul(p, p)

def cal(A, K):
    if K == 0: return I
    if K == 1: return A
    if K&1: return add(cal(A, K-1), pow(A, K))
    return mul(cal(A, K>>1), add(I, pow(A, K>>1)))

a = []
for i in range(n): a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n): a[i][j]%=10
B = cal(a, k)
for i in B:
    for j in i: print(j, end=' ')
    print()
