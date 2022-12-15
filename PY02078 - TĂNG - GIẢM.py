for t in range(int(input())):
    n, a = int(input()), []
    for i in range(n): a.append([float(x) for x in input().split()])
    ans = 1
    arr = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if a[i][0] > a[j][0] and a[i][1] < a[j][1]: arr[i] = max(arr[j] + 1, arr[i])
    print(max(arr))
