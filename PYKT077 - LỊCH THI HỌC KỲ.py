from datetime import date, datetime
class ob:
    def __init__(self, code, name) -> None:
        self.code = code
        self.name = name
class ob2(ob):
    def __init__(self, i, o, arr) -> None:
        self.code = f'T{str(i).zfill(3)}'
        self.ocode = o.code
        self.name = o.name
        self.date = datetime.strptime(arr[1], '%d/%m/%Y')
        self.strdate = arr[1]
        self.h = datetime.strptime(arr[2], '%H:%M')
        self.strh = arr[2]
        self.group = arr[3]
    def __str__(self) -> str:
        return self.code + ' ' + self.ocode + ' ' + self.name + ' ' + self.strdate + ' ' + self.strh + ' ' + self.group
n, m = map(int, input().split())
a, arr = {}, []
for i in range(n):
    s = input()
    a[s] = ob(s, input())
for i in range(m):
    line = input().split()
    arr.append(ob2(i+1, a[line[0]], line))
for i in sorted(arr, key=lambda x: (x.date, x.h, x.ocode)): print(i)
