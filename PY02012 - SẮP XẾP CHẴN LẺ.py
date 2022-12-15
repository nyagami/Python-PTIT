n = int(input())
a = []
while len(a)<n:
    a.extend(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]%2==0:
            if a[j]%2==0:
                if a[i]>a[j]:
                    tmp = a[i]
                    a[i] = a[j]
                    a[j] = tmp 
        else:
            if a[j]%2==1:
                if a[i]<a[j]:
                    tmp = a[i]
                    a[i] = a[j]
                    a[j] = tmp
for i in a: print(i,end=' ')
