a, n = [], int(input()) 
for i in range(n): a.append(input())
def turn(des, src):
    if des == src: return 0
    for i in range(len(des)):
        src = src[1:] + src[0]
        if src == des: return i+1
    return -1
ans = 10**5
check = True
for i in range(n):
    cnt = 0
    for j in range(n):
        if i!=j:
            num = turn(a[i], a[j])
            if num == -1:
                check = False
                break
            else: cnt += num
    ans = min(ans, cnt)
if check: print(ans)
else: print(-1)
