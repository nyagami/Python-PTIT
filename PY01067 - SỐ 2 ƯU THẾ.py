a = []
def Try(i, s, cnt2):
    if i==10: return
    if cnt2*2 > i: a.append(int(s))
    for c in '012': Try(i+1, s+c, cnt2+1 if c=='2' else cnt2)
Try(1,'1',0)
Try(1,'2',1)
a = sorted(a)
for t in range(int(input())):
    n = int(input())
    for i in range(n): print(a[i], end=' ')
    print()
