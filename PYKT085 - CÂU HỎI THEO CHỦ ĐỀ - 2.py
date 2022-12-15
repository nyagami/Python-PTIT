a = []
for i in range(int(input())): a.append(input())
while len(a)>0:
    ind = len(a)
    for i in range(len(a)):
        if a[i]=='':
            ind = i
            break
    print(f'{a[0]}: {ind-1}')
    a = a[ind+1:]
