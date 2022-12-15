import math
n,k = input().split()
arr=[x for x in range(10**(int(k)-1),10**int(k)) if math.gcd(x,int(n))==1]
for i in range(0,len(arr),10):
    print(' '.join([str(x) for x in arr[i:i+10]]))
