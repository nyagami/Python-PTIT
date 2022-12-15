from math import sqrt
def tn(x):
    s = str(x)
    if len(s) < 2: return False
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]: return False
    return True
a, ans, check, max = [], [], True, 2
n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if tn(a[i][j]):
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
