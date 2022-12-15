s1, s2 = input().split(), input().split()
s, u = set(), set()
for i in s1:
    s.add(i.lower())
    for j in s2:
        if i.lower()==j.lower(): u.add(i.lower())
for i in s2: s.add(i.lower())
print(' '.join(sorted(s)))
print(' '.join(sorted(u)))
