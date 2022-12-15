n, m = map(int, input().split())
a = sorted(set(map(int, input().split())))
b = sorted(set(map(int, input().split())))
for i in a:
    if b.count(i) > 0: print(i, end=' ')
print()
for i in a:
    if b.count(i) == 0: print(i, end=' ')
print()
for i in b:
    if a.count(i) == 0: print(i, end=' ')
