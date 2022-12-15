class ob:
    def __init__(self, i, name, a, b) -> None:
        self.code = f'TS0{str(i)}'
        self.name = name
        self.sum = ((a if a<=10 else a/10) + (b if b<=10 else b/10))/2
        if self.sum >= 9.5: self.type = 'XUAT SAC'
        elif self.sum >= 8: self.type = 'DAT'
        elif self.sum >= 5: self.type = 'CAN NHAC'
        else: self.type = 'TRUOT'
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + f'{round(self.sum, 2):.2f}' + ' ' + self.type
a = []
for i in range(int(input())): a.append(ob(i+1, input(), float(input()), float(input())))
for i in sorted(a, key=lambda x: -x.sum): print(i)
