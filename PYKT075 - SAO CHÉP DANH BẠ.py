from sys import stdin
def cleanName(name: str):
    a = name.lower().split()
    for i in range(len(a)): a[i] = a[i][0].upper() + a[i][1:].lower()
    return ' '.join(a)
class info:
    def __init__(self, day, name, sdt) -> None:
        self.day = day
        a = name.split()
        self.first = a[-1]
        self.mid = a[:-1]
        self.name = name
        self.sdt = sdt
    def __str__(self) -> str:
        return self.name + ': ' + self.sdt + ' ' + self.day
try: fr = open('SOTAY.txt', 'r')
except: fr = stdin
lines = [x.strip() for x in fr if x.strip() != '']
a = []
day = lines[0].split()[1]
i = 1
while i<len(lines): 
    s1 = lines[i]
    i+=1
    if s1.count('/') > 0:
        day = s1.split()[1]
        continue
    s2 = lines[i]
    i+=1
    a.append(info(day, cleanName(s1), s2))
for i in sorted(a, key=lambda x: (x.first, x.mid)): print(i)
