from datetime import datetime
class MT:
    def __init__(self, code, name, method) -> None:
        self.code = code 
        self.name = name 
        self.method = method 
class CA:
    def __init__(self, i, date, time, room) -> None:
        self.code = 'C' + str(i).zfill(3)
        self.strdate = date
        self.strtime = time
        self.date = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')
        self.room = room
class SCHE:
    def __init__(self, ca: CA, mt: MT, group, num) -> None:
        self.ca = ca
        self.mt = mt
        self.group = group
        self.num = num
    def __str__(self) -> str:
        return f'{self.ca.strdate} {self.ca.strtime} {self.ca.room} {self.mt.name} {self.group} {self.num}'
fmt = open('MONTHI.in')
fca = open('CATHI.in')
fsche = open('LICHTHI.in')
mmth, mca = {}, {}
n = int(fmt.readline().strip())
for i in range(n):
    x = MT(fmt.readline().strip(), fmt.readline().strip(), fmt.readline().strip())
    mmth[x.code] = x
m = int(fca.readline().strip())
for i in range(m):
    x = CA(i+1, fca.readline().strip(), fca.readline().strip(), fca.readline().strip())
    mca[x.code] = x
a = []
k = int(fsche.readline().strip())
for i in range(k):
    arr = fsche.readline().strip().split()
    x = SCHE(mca[arr[0]], mmth[arr[1]], arr[2], arr[3])
    a.append(x)
for i in sorted(a, key=lambda x: (x.ca.date, x.ca.code)): print(i)
