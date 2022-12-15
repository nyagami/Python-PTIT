n, m = map(int, input().split())
a = sorted(set(map(int, input().split())))
b = sorted(set(map(int, input().split())))
def check():
    if len(a) != len(b): return 'NO'
    for i in range(len(a)):
        if a[i] != b[i]: return 'NO'
    return 'YES'
print(check())
