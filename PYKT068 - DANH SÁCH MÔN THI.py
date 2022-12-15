class ob:
    def __init__(self, code, name, met) -> None:
        self.code = code
        self.name = name
        self.met = met
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + self.met
a = []
for i in range(int(input())): a.append(ob(input(), input(), input()))
for i in sorted(a, key=lambda x: x.code): print(i)
