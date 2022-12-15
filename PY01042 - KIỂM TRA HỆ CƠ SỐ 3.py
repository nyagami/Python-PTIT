for t in range(int(input())):
    def ans(n):
        for i in n:
            if '012'.find(i)==-1: return 'NO'
        return 'YES'
    print(ans(input()))
