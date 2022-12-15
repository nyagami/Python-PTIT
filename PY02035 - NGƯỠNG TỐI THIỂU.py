s = input()
k = int(input())
a = {}
while len(s) > 0:
    x = int(s[:2])
    if len(str(x)) == 2:
        if a.get(x) is None: a[x]=1
        else: a[x]+=1
    s = s[2:]
check = False
for i in sorted(a):
    if a[i]>=k:
        print(i, a[i])
        check = True
if not check: print('NOT FOUND')
