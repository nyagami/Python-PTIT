for t in range(int(input())):
    n, a, b = int(input()), sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())))
    def check():
        for i in range(n):
            if a[i] > b[i]: return 'NO'
        return 'YES'
    print(check())
