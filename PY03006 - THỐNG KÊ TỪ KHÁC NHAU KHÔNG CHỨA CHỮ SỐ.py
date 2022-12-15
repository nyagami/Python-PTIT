import re
a = {}
def allc(s):
    for i in s:
        if  '0'<=i and i<='9': return False
    return True
for i in range(int(input())):
    for s in re.split("[^a-z]", input().lower()):
        if s != '' and allc(s):
            if a.get(s) is None: a[s]=1
            else: a[s]+=1
ans = sorted(a, key=lambda x: (-a[x], x))
for i in ans: print(i, a[i])
