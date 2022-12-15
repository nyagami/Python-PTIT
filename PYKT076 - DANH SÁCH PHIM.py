from datetime import date, datetime
class ob:
    def __init__(self, i, name) -> None:
        self.code = f'TL{str(i).zfill(3)}'
        self.name = name
class ob2(ob):
    def __init__(self, i, type, date, nth, eps) -> None:
        self.code = f'P{str(i).zfill(3)}'
        self.type = type
        self.date = datetime.strptime(date, '%d/%m/%Y')
        self.strdate = date
        self.nth = nth
        self.eps = eps
    def __str__(self) -> str:
        return self.code + ' ' + self.type + ' ' + self.strdate + ' ' + self.nth + ' ' +self.eps
n, m = map(int, input().split())
a, arr = {}, []
for i in range(n):
    s = ob(i+1, input())
    a[s.code] = s.name
for i in range(m): arr.append(ob2(i+1, a[input()], input(), input(), input()))
for i in sorted(arr, key=lambda x: x.date): print(i)
