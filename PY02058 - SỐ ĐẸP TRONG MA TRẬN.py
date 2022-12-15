a, ans, check, Max, Min= [], [], True, 0, 10**5
n, m = map(int, input().split())
for i in range(n):
    arr = list(map(int, input().split()))
    Max = max(Max, max(arr))
    Min = min(Min, min(arr))
    a.append(arr)
for i in range(n):
    for j in range(m):
        if a[i][j] == Max-Min:
            check = False
            ans.append(f'Vi tri [{i}][{j}]')
if check: print('NOT FOUND')
else:
    print(Max-Min)
    print('\n'.join(ans))
