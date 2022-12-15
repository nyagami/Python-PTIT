import math
for ts in range(int(input())):
    n,x,m=[float(x) for x in input().split()]
    print(math.ceil(math.log(m/n,1+x/100)))
