from datetime import date
a = {}
def minute(s: str):
    h, m = s.split(':')
    return int(h)*60 + int(m)
class tp:
    name: str
    time: int
    water: int

    def __init__(self, n, start, end, m) -> None:
        self.name = n
        self.water = m
        self.time = minute(end) - minute(start)
t = 1
for i in range(int(input())):
    x = tp(input(), input(), input(), int(input()))
    if a.get(x.name) == None:
        x.code = 'T' + str(t).zfill(2)
        t+=1
        a[x.name] = x
    else:
        a[x.name].time += x.time
        a[x.name].water += x.water
for i in a:
    print(a[i].code, a[i].name, f'{a[i].water/(a[i].time/60):.2f}')
