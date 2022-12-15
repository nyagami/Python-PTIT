n, a, s = int(input()), [int(x) for x in input().split()], 0
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]: s+=1
print(s)
