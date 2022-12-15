def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])
class ob:
    def __init__(self, i, name, school) -> None:
        self.code = f'Team{str(i).zfill(2)}'
        self.name = name
        self.school = school
class ob2:
    def __init__(self, i, name, o) -> None:
        self.code = f'C{str(i).zfill(3)}'
        self.name = name
        self.o = o
    def __str__(self) -> str:
        return self.code + '  ' + self.name + ' ' + self.o.name + ' ' + self.o.school
team = {}
for i in range(int(input())):
    o = ob(i+1, input(), input())
    team[o.code] = o
a = []
for i in range(int(input())): a.append(ob2(i+1, input(), team[input()]))
for i in sorted(a, key=lambda x: x.name): print(i)
