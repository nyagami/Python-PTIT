n,x=input().split()
f=[1 for x in range(10002)]
f[0], f[1]=0 , 0
nt=[]
for i in range(2,10000):
    if f[i]:
        nt.append(i)
        for u in range(i,int(10000/i)): f[i*u]=0
pre = int(x)
print(x, end=' ')
for i in range(int(n)):
    print(pre+nt[i],end=' ')
    pre += nt[i]
    
