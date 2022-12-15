from datetime import datetime
price = {'1': 25, '2': 34, '3': 50, '4': 80}
class ob:
    def __init__(self, i, name, room, d1, d2, plus) -> None:
        self.code = f'KH{str(i).zfill(2)}'
        self.name = name
        self.room = room
        self.days = (datetime.strptime(d2, "%d/%m/%Y") -
                     datetime.strptime(d1, "%d/%m/%Y")).days + 1
        self.plus = plus
        self.sum  = self.days * price[self.room[0]] + self.plus
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.room + ' ' + str(self.days) + ' ' +str(self.sum) 
a = []
for i in range(int(input())):
    a.append(ob(i+1, input(), input(), input().strip(), input().strip(), int(input())))
for i in sorted(a, key=lambda x: -x.sum): print(i)
