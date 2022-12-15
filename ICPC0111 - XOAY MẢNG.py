for t in range(int(input())):
    n, d = map(int, input().split())
    a = input().split()
    print(' '.join(a[d:]), ' '.join(a[:d]))
