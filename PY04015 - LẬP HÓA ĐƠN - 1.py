class kh:
    def __init__(self, i, n, pre, af) -> None:
        self.code = f'KH{str(i).zfill(2)}'
        self.name = n
        m = af - pre
        if m > 100: self.bill = ((m-100)*200 + 50*(100+150))*1.05
        elif m > 50: self.bill = ((m-50)*150 + 50*100)*1.03
        else: self.bill = m*100*1.02
a = []
for t in range(int(input())):
    a.append(kh(t+1,input(), int(input()), int(input())))
a.sort(key = lambda x: (-x.bill, x.code))
for i in a: print(i.code, i.name, f'{i.bill:.0f}')
