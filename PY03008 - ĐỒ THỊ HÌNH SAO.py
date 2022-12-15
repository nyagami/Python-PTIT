n = int(input())
a = {str(i+1):0 for i in range(n)}
for i in range(n-1):
    x, y = input().split()
    a[x]+=1
    a[y]+=1
cnt = 0
for i in a: cnt += 1 if a[i]==1 else 0
print('Yes' if cnt == n-1 else 'No')
