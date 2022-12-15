price = {
    '5': 10000,
    '7': 15000,
    '2': 20000,
    '29': 50000,
    '45': 70000
}
a = {}
for i in range(int(input())):
    arr = input().split()
    if arr[-2] == 'OUT': continue
    if a.get(arr[-1]) is None: a[arr[-1]] = price[arr[-3]]
    else: a[arr[-1]] += price[arr[-3]]
for i in sorted(a): print(f'{i}: {a[i]}')
