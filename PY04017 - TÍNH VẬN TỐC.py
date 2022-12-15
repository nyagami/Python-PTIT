from datetime import datetime
import math
class ob:
    def __init__(self, name, address, end) -> None:
        self.name = name
        self.address = address
        self.time = (datetime.strptime(end, '%H:%M') - datetime.strptime('6:00', '%H:%M')).seconds/3600
        self.v = 120/(self.time)
        self.code = ''
        for i in address.split(): self.code += i[0].upper()
        for i in name.split(): self.code += i[0].upper()
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.address + ' ' + f'{round(self.v)} Km/h'
a = []
for i in range(int(input())): a.append(ob(input(), input(), input()))
for i in sorted(a, key=lambda x: x.time): print(i)
