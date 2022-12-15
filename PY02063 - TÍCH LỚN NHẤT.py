n, a = int(input()), sorted(list(map(int, input().split())))
ans2, ans3 = a[-2]*a[-1], a[-2]*a[-1]*a[-3]
ans2 = max(ans2, a[0]*a[1])
ans3 = max(ans3, a[0]*a[1]*a[-1])
print(max(ans2, ans3))
