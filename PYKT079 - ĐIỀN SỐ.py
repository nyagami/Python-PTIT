for t in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    Max, Min, total = max(a), min(a), 0
    if Max - Min <= 1: print(0)
    else:
        dic = {Max:1, Min:1}
        for i in a:
            if dic.get(i) is None:
                total+=1
                dic[i]=1
        print(Max - Min -1 -total)
