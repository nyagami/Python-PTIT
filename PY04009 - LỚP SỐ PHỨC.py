for t in range(int(input())):
    a = list(map(int, input().split()))
    x, y =complex(a[0],a[1]), complex(a[2], a[3])
    c, d = (x+y)*x, (x+y)*(x+y)
    a = list(map(int, [c.real, c.imag, d.real, d.imag]))
    print(f'{a[0]} + {a[1]}i, {a[2]} + {a[3]}i')
