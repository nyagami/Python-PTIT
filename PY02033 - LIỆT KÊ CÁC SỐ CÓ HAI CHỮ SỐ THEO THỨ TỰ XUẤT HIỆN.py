s = input()
a = []
while len(s) > 0:
    x = int(s[:2])
    if len(str(x)) == 2:
        if a.count(x) == 0: a.append(x)
    s = s[2:]
for i in a: print(i, end=' ')
