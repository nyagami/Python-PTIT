arr = []
a,k,n = [int(x) for x in input().split()]
for i in range(0,n+1,k):
    if i>a: arr.append(str(i-a))
print(-1) if arr==[] else print(' '.join(arr))
