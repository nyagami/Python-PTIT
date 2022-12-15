class sv:
    def __init__(self, msv, name, cl) -> None:
        self.msv = msv
        self.name = name
        self.cl = cl
    def cal(self, s: str):
        m = s.count('m')
        v = s.count('v')
        self.cc = max(0, 10 - m - v*2)
    def __str__(self) -> str:
        return self.msv + ' ' + self.name + ' ' + self.cl + ' ' + str(self.cc) + (' KDDK' if self.cc == 0 else '')
a = {}
n = int(input())
for i in range(n):
    x = sv(input(), input(), input())
    a[x.msv] = x
for i in range(n):
    msv, s = input().split()
    a[msv].cal(s)
for i in a:
    print(a[i])
