from sys import stdin
# stdin = open("d:/code/in.txt")
n = int(stdin.readline())
a = [i for i in map(float, stdin.readline().split())]

def weak(X):
    pos, neg, prep, pren = 0.0, 0.0, 0.0, 0.0
    for i in a:
        b = i - X
        prep += b
        pren += b
        if prep > 0.0:
            if prep > pos: pos = prep
        else: prep = 0.0
        if pren < 0.0:
            if pren < neg: neg = pren
        else: pren = 0.0
    return round(pos, 6), round(-neg, 6)
        
def main():
    l, r = min(a), max(a)
    pos, neg = 1.0, 0.0
    while pos != neg:
        mid = (l + r) / 2
        pos, neg = weak(mid)
        if pos > neg: l = mid
        else: r = mid
    print(f'{pos:.6f}')
main()
