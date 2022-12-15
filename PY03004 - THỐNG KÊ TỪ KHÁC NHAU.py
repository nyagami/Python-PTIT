import re
a = {}
for i in range(int(input())):
    for s in re.split("[^a-z0-9]", input().lower()):
        if s != '':
            if a.get(s) is None: a[s]=1
            else: a[s]+=1
ans = sorted(a, key=lambda x: (-a[x], x))
for i in ans: print(i, a[i])
