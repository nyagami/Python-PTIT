n = input()
a = []
while True:
    try:
        arr = list(map(int, input().split()))
        a.extend(arr)
    except: break
a.sort()
check = True
for i in range(1, a[-1]):
    if a.count(i) == 0:
        check = False
        print(i)
if check: print('Excellent!')
