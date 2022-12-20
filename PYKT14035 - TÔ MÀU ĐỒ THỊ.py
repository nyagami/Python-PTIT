from sys import stdin, setrecursionlimit
# stdin = open('d:/code/in.txt')
setrecursionlimit(100000)
limit = 15
sample = list(range(limit))
g = []
def dfs(node):
    c = sample.copy()
    for x in g[node]:
        nxt, f_min, s_min = dfs(x)
        c[f_min] += nxt[s_min]
        for i in range(1, f_min): c[i] += nxt[f_min]
        for i in range(f_min + 1, limit): c[i] += nxt[f_min]

    f_min, s_min = 1, 2
    for i in range(1, limit):
        if c[f_min] > c[i]:
            s_min = f_min
            f_min = i
        elif c[s_min] > c[i] and i^f_min: s_min = i
    return c, f_min, s_min

for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    g = [[] for i in range(n+1)]
    a = [int(x) for x in stdin.readline().split()]
    for i in range(n): g[a[i]].append(i + 1)
    ans, f_min, s_min = dfs(1)
    print('Case #' + str(t + 1) + ': ' + str(ans[f_min]))
