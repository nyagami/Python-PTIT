while True:
    n = int(input())
    if n==0: break
    a=set([n])
    while n!=1:
        if n%2==0: n=int(n/2)
        else: n=n*3+1
        a.add(n)
    print(len(a))
