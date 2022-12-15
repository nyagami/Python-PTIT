n = int(input())
a = [2,3,5,7]
ans = set()
def ok(check):
    for i in check:
        if not i: return False
    return True

def Try(check, s):
    if len(s)>=4 and ok(check) and s[-1]!='2': ans.add(int(s))
    if len(s) == n: return
    for i in range(4):
        tmp = [i for i in check]
        tmp[i] = True
        Try(tmp, s+str(a[i]))
Try([False, False, False, False], '')
for i in sorted(ans): print(i)
