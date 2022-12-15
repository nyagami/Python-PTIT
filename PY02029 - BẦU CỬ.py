n, m = map(int, input().split())
a = list(map(int, input().split()))
mp = {}
for i in a:
    if mp.get(i) is None: mp[i] = 1
    else: mp[i] += 1
a = sorted(mp, key=lambda x: (-mp.get(x), x))
Max = mp[a[0]]
while len(a)>0 and mp[a[0]]==Max: a.pop(0)
if len(a)==0: print('NONE')
else: print(a[0])
