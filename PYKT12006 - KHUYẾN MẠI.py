n, k = map(int, input().split())
a1, a2 = list(map(int, input().split())), list(map(int, input().split()))
a = [[]]*n
for i in range(n):
    a[i] = [a1[i], a2[i]]
a.sort(key=lambda x: x[0]-x[1])
ans = 0
for i in range(k): ans+=a[i][0]
i = k
while i<n and a[i][0] < a[i][1]:
    ans += a[i][0]
    i+=1
for j in range(i, n): ans += a[j][1]
print(ans)
