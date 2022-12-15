n, a, st = input(), list(map(int, input().split())), []
for i in a:
    if len(st) == 0 or (st[-1]+i)&1: st.append(i)
    else: st.pop(-1)
print(len(st))
