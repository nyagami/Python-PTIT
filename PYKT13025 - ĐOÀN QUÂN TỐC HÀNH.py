n, k = map(int, input().split())
a = map(int, input().split())
cnt = [0]*k
for i in a: cnt[i-1] += 1
a = []
for i in cnt:
    if i: a.append(i)
a.sort()
k = len(a)

def get(box):
    L, R, res = 0, k - 1, 0
    while L <= R:
        res += 1
        if L == R:
            break
        if a[L] + a[R] > box:
            R -= 1
        else:
            L += 1
            R -= 1
    return res * box
l, r = a[-1], min(a[-1] + 500, a[-1]*2)
ANS = get(l)
for i in range(l + 1, r):
    ANS = min(ANS, get(i))
print(ANS)
