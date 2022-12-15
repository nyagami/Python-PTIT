def cal(arr):
    a = list(reversed(arr))
    st = []
    while len(a) > 0:
        x = a.pop()
        if x == '*':
            i = a.pop()
            u = st.pop()
            st.append(str(int(i)*int(u)))
        else: st.append(x)
    s = int(st[0])
    for i in range(1, len(st), 2):
        op = st[i]
        b = st[i+1]
        if op == '+': s+=int(b)
        else: s-=int(b)
    return s
ok = False
def Try(i, n, m, a, arr):
    if i == n-1:
        if cal(arr) == m:
            global ok
            ok = True
            for x in arr:
                if len(x) > 1 and x[0] == '-': print(f'({x})', end='')
                else: print(x, end='')
            print(f'={m}')
        return
    for op in '+-*': Try(i+1, n, m, a, arr + [op, a[i+1]])
    
n, m = map(int, input().split())
a = input().split()
Try(0, n, m, a, [a[0]])
if not ok: print('IMPOSSIBLE')
