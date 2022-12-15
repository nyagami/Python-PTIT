def dt(s):
    if s.lower()=='kinh': return 0
    return 1.5
def sup(s):
    if s=='1': return 1.5
    if s=='2': return 1
    return 0
def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])
class ob:
    def __init__(self, i, name, sum, p, kv) -> None:
        self.code = f'TS{str(i).zfill(2)}'
        self.name = cleanName(name)
        self.sum = sum + sup(kv) + dt(p)
        if self.sum >= 20.5: self.type = 'Do'
        else: self.type = 'Truot'
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + f'{self.sum:.1f}' + ' ' + self.type
a = []
for i in range(int(input())): a.append(ob(i+1, input(), float(input()), input(), input()))
for i in sorted(a, key=lambda x: -x.sum): print(i)
