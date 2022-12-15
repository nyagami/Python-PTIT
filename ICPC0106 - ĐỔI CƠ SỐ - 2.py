from math import log2
def toS(i):
    if i<=9: return str(i)
    return chr(ord('A') + i-10)
def convert(s):
    r = 0
    for i in s: r = r<<1 | int(i)
    return toS(r)
for t in range(int(input())):
    b = int(log2(int(input())))
    s = input()
    r = ''
    while s!='':
        r = convert(s[-b:]) + r
        s = s[:-b]
    print(r)
