f = open('VANBAN.in', 'r')
class pair:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def len(self): return len(self.s)
def check(s):
    for i in range(len(s)>>1):
        if s[i] != s[len(s)-1-i]: return False
    return True
a = f.read().split()
m = {}
for i in range(len(a)):
    if check(a[i]):
        if m.get(a[i]) is None:
            x = pair(1, i)
            m[a[i]] = x
        else: m[a[i]].x += 1
a = sorted(m, key=lambda x: (-len(x), m[x].y))
for i in a: 
    if len(i) == len(a[0]): print(i, m[i].x)
