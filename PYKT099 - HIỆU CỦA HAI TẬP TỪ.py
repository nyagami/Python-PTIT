with open("DATA1.in") as f: set1 = set(f.read().lower().split())
with open("DATA2.in") as f: set2 = set(f.read().lower().split())
print(' '.join(sorted(set1.difference(set2))))
print(' '.join(sorted(set2.difference(set1))))
