from sys import stdin
n=int(stdin.readline())
a = list(map(int, stdin.readline().split()))
ans = 10**18
for i in range(n) :
    change = 0
    b = a.copy()
    # for j in range(n):
    #     b[j] += abs(j - i) - i
    for j in range(i):
        b[j] += change
        change-=1
    for j in range(i,n) :
        b[j] += change
        change += 1
    b.sort()
    top = max(b[n//2], -change, 0) + i
    steps = 0
    for j in range(i):
        steps += abs(top - abs(i-j) - a[j])
    for j in range(i,n) :
        steps += abs(top - abs(i-j) - a[j])
    ans = min(ans, steps)
print(ans)
