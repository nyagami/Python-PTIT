def std(i):
    if i<=9: return i
    return chr(ord('A') + i - 10)
for t in range(int(input())):
    a, b = map(int, input().split())
    i = 0 
    while a >= b**i: i+=1
    i-=1
    for j in range(i+1):
        c = a//(b**i)
        print(std(c), end='')
        a = a - c*(b**i)
        i-=1
    print()
