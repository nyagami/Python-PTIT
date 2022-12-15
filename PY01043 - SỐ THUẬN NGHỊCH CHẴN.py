arr = []
def Try(i,n,s):
    if s!= "" and s[0]=='0': return
    if i==n: return arr.append(s+''.join(reversed(s)))
    for j in range(0,9,2): Try(i+1,n,s+str(j))
for i in range(1,5): Try(0,i,'')

for t in range(int(input())):
    n=int(input())
    print(' '.join([x for x in arr if(int(x)<n)]))
