from math import sqrt
for t in range(int(input())):
    n, p = map(int, input().split())
    cnt = 0
    for i in range(1,n+1):
        while i%p==0:
            cnt+=1
            i/=p
    print(cnt)
            
