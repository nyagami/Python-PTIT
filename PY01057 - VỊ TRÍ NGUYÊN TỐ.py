nt = [1 for x in range(505)]
nt[0]=nt[1]=0
for i in range(2,505):
    if nt[i]:
        for u in range(i,int(505/i)): nt[i*u]=0
def c(s):
    for i in range(len(s)):
        if nt[i] and nt[int(s[i])]: continue
        if not nt[i] and not nt[int(s[i])]: continue
        return 'NO'
    return 'YES'
for t in range(int(input())):
    print(c(input()))
