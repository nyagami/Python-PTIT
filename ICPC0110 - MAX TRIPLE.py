from sys import stdin
c, e = 0, -10**9
# stdin = open('d:/code/in.txt')
for t in range(int(stdin.readline())):
    stdin.readline()
    l = stdin.readline()
    x, y, z = [e, e, e]
    n = len(l)//3
    while l[n] != ' ': n-=1
    a = l[:n]
    l = l[n:]
    for i in map(int, a.split()): 
        if i>=x:
            z = y
            y = x
            x = i
        elif i>=y:
            z = y 
            y = i
        elif i>z: z = i
    n = len(l)>>1
    while l[n] != ' ': n-=1
    for i in map(int, l[:n].split()):
        if i <= z: continue
        if i>=x:
            z = y
            y = x
            x = i
        elif i>=y:
            z = y 
            y = i
        else: z = i
    for i in map(int, l[n:].split()):
        if i>=x:
            z = y
            y = x
            x = i
        elif i>=y:
            z = y 
            y = i
        elif i>z: z = i
    print(x+y+z)
