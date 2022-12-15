f = open('DATA.in', 'r')
a = []
for line in f:
    for j in line.split():
        try:
            x = int(j)
            if x > (1<<63): a.append(j)
        except: a.append(j)
print(' '.join(sorted(a)))
