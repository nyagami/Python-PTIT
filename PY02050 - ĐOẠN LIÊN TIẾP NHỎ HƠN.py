for t in range(int(input())):
    n, arr = int(input()), [int(x) for x in input().split()]
    st = []
    for i in range(n):
        arr[i] = (arr[i], i)
        while len(st)>0 and st[len(st)-1][0]<=arr[i][0]: 
            arr[i] = (arr[i][0],st[len(st)-1][1])
            st.pop()
        st.append(arr[i])
    for i in range(n):
        print(i-arr[i][1]+1, end=' ')
    print('')
