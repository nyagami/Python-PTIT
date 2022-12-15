n, ans = int(input()), 0
a = []
for i in range(n): a.append(input())
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            for k in range(i+1, n): ans += 1 if a[k][j] == 'C' else 0
            for k in range(j+1, n): ans += 1 if a[i][k] == 'C' else 0
print(ans)
