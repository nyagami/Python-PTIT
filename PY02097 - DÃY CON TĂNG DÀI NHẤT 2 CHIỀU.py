from sys import stdin
# stdin = open("D:/code/in.txt")

def first(x, a):
    l, r = 0, len(a)
    if r < 12:
        for i in reversed(range(r)):
            if a[i][0] < x: return i + 1
        return 0
    else:
        while l < r:
            mid = (l + r) // 2
            if a[mid][0] < x: l = mid + 1
            else: r = mid
        return l

def second(N, x, a):
    return N and a[N-1][1] < x

def main():
    _all = map(int, stdin.read().split())
    stdin.close()
    LEN = []
    for _ in range(next(_all)):
        l, r, x = 0, len(LEN), (next(_all), next(_all))
        while l < r:
            mid = (l + r) // 2
            a = LEN[mid]
            if a and second(first(x[0], a), x[1], a): l = mid + 1
            else: r = mid
        if l == len(LEN): LEN.append([x])
        else:
            LL = LEN[l]
            LLL = len(LL)
            st = ed = first(x[0], LL)
            while ed < LLL and x[1] <= LL[ed][1]: ed +=1
            del LL[st:ed]
            LL.insert(st, x)
    print(len(LEN))
main()
