input()
a = sorted([float(x) for x in input().split()])
s = 0
b = [x for x in a if x!=a[0] and x!=a[-1]]
for x in b: s+=x
print(f"{s/len(b):.2f}")
