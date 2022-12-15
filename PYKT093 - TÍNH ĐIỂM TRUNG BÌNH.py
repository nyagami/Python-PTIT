from math import ceil
def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])
class ob:
    def __init__(self, i, name, m1, m2, m3) -> None:
        self.code = f'SV{str(i).zfill(2)}'
        self.name = cleanName(name)
        self.sum = (m1*3 + m2*3 + m3*2)/8
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + f'{(ceil(self.sum*100)/100):.2f}' + ' ' + str(self.type)
a = []
for i in range(int(input())): a.append(ob(i+1, input(), float(input()), float(input()), float(input())))
a.sort(key=lambda x: -x.sum)
a[0].type = 1
rank, pre = 1, a[0]
for i in a:
    if i.sum < pre.sum:
        i.type = rank
        pre = i
    else:
        i.type = pre.type
    print(i)
    rank+=1
