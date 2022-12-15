import math


for t in range(int(input())):
    print('1',end='')
    n = int(input())
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            cnt=0
            while(n%i==0):
                cnt+=1
                n/=i
            print(f' * {i}^{cnt}',end='')
    if(n>1): print(f' * {int(n)}^1',end='')
    print('')
