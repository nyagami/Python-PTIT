n = int(input())
arr = sorted([int(x) for x in input().split()])
for i in range(1,n+1):
    try: arr.index(i)
    except:
        print(i)
        n=0
        break
if n!=0: print(n+1)
