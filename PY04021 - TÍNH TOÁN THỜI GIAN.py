from datetime import datetime
class per:
    def __init__(self, code, name, tin, tout) -> None:
        self.code = code
        self.name = name
        self.time = datetime.strptime(tout, '%H:%M') - datetime.strptime(tin, '%H:%M')
a = []
for i in range(int(input())):
    a.append(per(input(),input(),input(),input()))
a.sort(key=lambda x: -x.time)
for i in a:
    print(i.code, i.name, i.time.seconds//3600, 'gio', i.time.seconds//60%60, 'phut')
