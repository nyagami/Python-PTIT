a = []
class stu:
    def __init__(self, n, a, s) -> None:
        self.name = n
        self.ac = a
        self.submit = s
for i in range(int(input())):
    name = input()
    ac, submit = input().split()
    a.append(stu(name, int(ac), int(submit)))
a = sorted(a, key = lambda x: (-x.ac, x.submit, x.name))
for i in a: print(i.name, i.ac, i.submit)
