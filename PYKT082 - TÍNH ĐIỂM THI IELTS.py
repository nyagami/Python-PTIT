def p(x):
    if x>38: return 9.0
    if x>36: return 8.5
    if x>34: return 8.0
    if x>32: return 7.5
    if x>29: return 7.0
    if x>26: return 6.5
    if x>22: return 6.0
    if x>19: return 5.5
    if x>15: return 5.0
    if x>12: return 4.5
    if x>9: return 4.0
    if x>6: return 3.5
    if x>4: return 3.0
    if x>2: return 2.5
    return 1.0
def r(x):
    ext = x - int(x)
    if ext >= 0.75: return int(x) + 1.0
    if ext >= 0.25: return int(x) + 0.5
    return float(int(x))
for t in range(int(input())):
    a = input().split()
    s = (p(int(a[0])) + p(int(a[1])) + float(a[2]) + float(a[3]))/4
    print(r(s))
