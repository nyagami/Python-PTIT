n, a = int(input()), list(map(int, input().split()))
ind, Min = 0, 100000000
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(a[i]-a[j])
    if sum < Min:
        ind = i
        Min = sum
print(Min, a[ind])
