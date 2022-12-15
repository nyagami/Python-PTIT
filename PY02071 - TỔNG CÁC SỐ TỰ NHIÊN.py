ans = []
def Try(start, n, sum, s):
    if sum == n:
        ans.append(f'({s[:-1]})')
    if sum > n: return
    for i in range(start, 0, -1): Try(i, n, sum+i, s + f'{i} ')

for t in range(int(input())):
    ans = []
    n = int(input())
    Try(n, n, 0, '')
    print(len(ans))
    print(' '.join(ans))
