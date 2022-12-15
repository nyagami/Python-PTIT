from math import sqrt
def nt(x):
    if x<2: return False
    if x==2: return True
    if x%2==0: return False
    for i in range(3, int(sqrt(x))+1, 2):
        if x%i==0: return False
    return True
a, ans, check, max = [], [], True, 2
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            check = False
            if a[i][j] == max: ans.append((i, j))
            elif a[i][j] > max:
                ans = [(i, j)]
                max = a[i][j]
if check: print('NOT FOUND')
else:
    print(max)
    for i in ans:
        print(f'Vi tri [{i[0]}][{i[1]}]')
