s = input()
a = set()
while len(s) > 0:
    x = int(s[:2])
    if len(str(x)) == 2: a.add(x)
    s = s[2:]
for i in sorted(a): print(i, end=' ')
