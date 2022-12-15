def cleanName(s):
    return ' '.join([(x[0].upper() + x[1:].lower()) for x in s.split()])
def x(s):
    y = int(s[1:3])
    if 1<=y and y<=3:
        if s[0]=='A': return 10
        elif s[0]=='B': return 10
        elif s[0]=='C': return 9
        return 8
    elif 4<=y and y<=8:
        if s[0]=='A': return 12
        elif s[0]=='B': return 11
        elif s[0]=='C': return 10
        return 9
    elif 9<=y and y<=15:
        if s[0]=='A': return 14
        elif s[0]=='B': return 13
        elif s[0]=='C': return 12
        return 11
    else: 
        if s[0]=='A': return 20
        elif s[0]=='B': return 16
        elif s[0]=='C': return 14
        return 13
class ob:
    def __init__(self, s) -> None:
        s = s.split()
        self.code = s[0]
        self.name = ' '.join(s[1:])
class ob2:
    def __init__(self, code, name, sday, days, o) -> None:
        self.code = code
        self.name = name
        self.sum = sday*days*x(code)*10**3
        self.o = o
    def __str__(self) -> str:
        return self.code + '  ' + self.name + ' ' + self.o.name + ' ' + str(self.sum)
m = {}
for i in range(int(input())):
    o = ob(input())
    m[o.code] = o
a = []
for i in range(int(input())): 
    code = input()
    a.append(ob2(code, input(), int(input()), int(input()), m[code[3:]]))
for i in a: print(i)
