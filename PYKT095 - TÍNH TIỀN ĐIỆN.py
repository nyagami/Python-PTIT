def cleanName(s):
    return ' '.join([x[0].upper() + x[1:].lower() for x in s.split()])
def dm(s):
    if s=='A': return 100
    if s=='B': return 500
    return 200
class ob:
    def __init__(self, i, s, a) -> None:
        self.code = f'KH{str(i).zfill(2)}'
        self.name = cleanName(s)
        self.dm = dm(a[0])
        self.dis = int(a[2]) - int(a[1])
        self.indm = min(self.dis, self.dm)*450
        self.outdm = max(self.dis-self.dm, 0)*1000
        self.vat = self.outdm//20
        self.sum = self.indm + self.outdm + self.vat
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + f'{self.indm} {self.outdm} {self.vat} {self.sum}'
a = []
for i in range(int(input())): a.append(ob(i+1, input(), input().split()))
for i in sorted(a, key=lambda x: -x.sum): print(i)
