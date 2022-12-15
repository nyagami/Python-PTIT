f = open('CONTACT.in', 'r')
a = set()
for line in f: a.add(line.strip().lower())
print('\n'.join(sorted(a)))
