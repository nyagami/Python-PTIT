def tcs(x):
    s=1
    for i in x: s*=int(i)
    return s
for t in range(int(input())):
    input()
    for i in sorted([(tcs(x),int(x)) for x in input().split()]): print(i[1], end=' ')
    print('')
