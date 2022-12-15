def low(a, l, r, x):
    while l<r:
        mid = (l+r)>>1
        if a[mid] < x: l = mid + 1
        else: r = mid
    return l
def first_big(a, arr):
    st = []
    for i in range(1, len(a)):
        if len(st) == 0:
            arr[i] = 0
            st.append(i)
        else:
            while len(st) > 0 and a[st[-1]] <= a[i]: st.pop()
            if len(st) == 0: arr[i] = 0
            else: arr[i] = st[-1]
            st.append(i)
test = int(input())
e = []
while True:
    try: e.extend(map(int, input().split()))
    except: break
I = 0
for t in range(test):
    n = e[I]
    I+=1
    l = [-1] + e[I:I+n]
    I+=n
    h = [0] + e[I:I+n]
    I+=n

    left = [0]*(n+1)
    first_big(h, left)

    Vn, Vw = [0]*(n+2), [0]*(n+2)
    for i in range(1,n+1):
        if h[i] > h[i-1]: 
            Vn[i] = Vn[left[i]] + h[i]*(l[i] - l[left[i]] - 1) - (Vw[i-1] - Vw[left[i]])
        else: Vn[i] = Vn[i-1] + h[i]*(l[i] - l[i-1] - 1)
        Vw[i] = Vw[i-1] + h[i]
    Vn[n+1] = 10**18
    Q = e[I]
    I+=1
    for q in range(Q):
        k = e[I+q]
        print(low(Vn, 1, n+1, k) - 1)
    I+=Q
