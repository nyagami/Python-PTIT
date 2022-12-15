from itertools import combinations

n, k = map(int, input().split())
a = sorted(set(input().split()))
ans = combinations(a, k)
for i in ans: print(' '.join(i))
