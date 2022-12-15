def sub(s):
    if s[0]=='A': return 'TOAN'
    if s[0]=='B': return 'LY'
    return 'HOA'
def sup(s):
    if s[1]=='1': return 2
    if s[1]=='2': return 1.5
    if s[1]=='3': return 1
    return 0
class ob:
    def __init__(self, i, name, code, t, c) -> None:
        self.code = f'GV{str(i).zfill(2)}'
        self.name = name
        self.sub = sub(code)
        self.sum = sup(code) + t*2 + c
        if self.sum >= 18: self.type = 'TRUNG TUYEN'
        else: self.type = 'LOAI'
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.sub + ' ' + f'{self.sum:.1f}' + ' ' + self.type
a = []
for i in range(int(input())): a.append(ob(i+1, input(), input(), float(input()), float(input())))
for i in sorted(a, key=lambda x: -x.sum): print(i)
