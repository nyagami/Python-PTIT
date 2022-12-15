class ob:
    def __init__(self, code, name, num, price, ck) -> None:
        self.code = code
        self.name = name
        self.num = num
        self.price = price
        self.ck = ck
        self.sum = num*price - ck
    def __str__(self) -> str:
        return self.code + ' ' + self.name + ' ' + str(self.num) + ' ' + str(self.price) + ' ' + str(self.ck) + ' ' + str(self.sum) 
a = []
for i in range(int(input())): a.append(ob(input(), input(), int(input()), int(input()), int(input())))
for i in sorted(a, key=lambda x: -x.sum): print(i)
