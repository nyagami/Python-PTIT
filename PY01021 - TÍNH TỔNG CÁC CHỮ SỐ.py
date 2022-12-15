from functools import reduce
for t in range(int(input())):
    s = input()
    sum = 0 
    a = []
    for i in s:
        if '0'<=i and i<='9': sum+=int(i)
        else: a.append(i) 
    print(''.join(sorted(a)) + str(sum))
