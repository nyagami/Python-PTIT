def to(i):
    s = 0 
    for j in i: s = s<<1 | int(j)
    return str(s)
s = input()
ans = []
while s != '':
    ans.insert(0, to(s[-3:]))
    s = s[:-3]
print(''.join(ans))
