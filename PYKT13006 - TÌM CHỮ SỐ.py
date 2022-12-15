mod = 1000
class pair:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'{self.x} {self.y}'
def mul(a, b):
    r = pair(0, 0)
    r.x = (a.x*b.x + 5*a.y*b.y)%mod
    r.y = (a.x*b.y + a.y*b.x)%mod
    return r
def pow(a, b):
    if b == 0: return pair(1, 0)
    if b&1: return mul(pow(a, b-1), a)
    p = pow(a, b>>1)
    return mul(p, p)
x = pair(3, 1)
for t in range(int(input())):
    print(f'Case #{t+1}: ',end='')
    print(str(pow(x, int(input())).x*2%mod - 1).zfill(3))
