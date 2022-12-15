from sys import stdin
from math import sqrt
def dis(v): return sqrt(v[0]*v[0] + v[1]*v[1])
def cos(u, v): return (u[0]*v[0]+u[1]*v[1])/(dis(u) * dis(v))
def same(u, v): return u[0] == v[0] and u[1] == v[1]
def area(hull):
    s, n = 0, len(hull)
    j = n - 1
    for i in range(n):
        xi, yi = hull[i]
        xj, yj = hull[j]
        s += (xj + xi)*(yj - yi)
        j = i
    return abs(s)/2
for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = []
    for i in range(n): a.append(list(map(int, stdin.readline().split())))
    a.sort(key=lambda x: (x[1], x[0]))
    s = a[-1]
    hull = [s]
    pre = s
    pre_v = (1, 0)
    while(True):
        cur_cos = -1
        cur_ind = 0
        for i in range(n):
            if same (pre, a[i]): continue
            cur_v = (a[i][0] - pre[0], a[i][1] - pre[1])
            cos_v = cos(cur_v, pre_v)
            if cos_v >= cur_cos:
                cur_cos = cos_v
                cur_ind = i

        pre_v = (a[cur_ind][0] - pre[0], a[cur_ind][1] - pre[1])
        pre = a[cur_ind]
        if same(pre, s): break
        hull.append(a[cur_ind])
    print(f'{area(hull):.3f}')
