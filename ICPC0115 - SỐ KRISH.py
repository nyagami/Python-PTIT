def gt(x):
    if x==0: return 1
    return x*gt(x-1)
for t in range(int(input())):
    s = input()
    sum = 0
    for i in s: sum += gt(int(i))
    print('Yes') if sum == int(s) else print('No')
