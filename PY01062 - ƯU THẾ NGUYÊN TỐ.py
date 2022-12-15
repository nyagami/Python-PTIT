nt = [1 for x in range(10005)]
nt[0]=nt[1]=0
for i in range(2,10005):
    if nt[i]:
        for u in range(i,int(10005/i)): nt[i*u]=0

def c(s):
    if not nt[len(s)]: return 'NO'
    if len([x for x in s if nt[int(x)]])*2>len(s): return 'YES'
    return 'NO'
for t in range(int(input())):
    print(c(input()))
