from datetime import datetime
class ca:
    def __init__(self, i, date, time, room) -> None:
        self.code = 'C' + str(i).zfill(3)
        self.date = date
        self.time = time
        self.room = room
        self.dtime = datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')
    def __str__(self) -> str:
        return self.code + ' ' + self.date + ' ' + self.time + ' ' + self.room
a = []
f = open('CATHI.in', 'r')
for i in range(int(f.readline())): a.append(ca(i+1, f.readline().strip(), f.readline().strip(), f.readline().strip()))
a.sort(key=lambda x: (x.dtime, x.code))
for i in a: print(i)
