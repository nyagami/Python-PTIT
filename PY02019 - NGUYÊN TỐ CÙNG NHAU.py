from math import gcd
n, arr = int(input()), [int(x) for x in input().split()]
arr = sorted(arr)
for i in range(n):
    for j in range(i+1,n):
        if gcd(arr[i],arr[j])==1: print(f'{arr[i]} {arr[j]}')
