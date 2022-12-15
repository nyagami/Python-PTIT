for t in range(int(input())):
    a={}
    for i in range(int(input())):
        x = int(input())
        if a.get(x): a[x]+=1
        else: a[x]=1
    a=sorted(a, key=lambda x: (-a[x],x))
    print(a[0])
