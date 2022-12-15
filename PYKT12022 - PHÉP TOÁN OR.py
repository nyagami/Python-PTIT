n, a = int(input()), list(map(int, input().split()))
s, ans = set(), set()
for i in a:
    new_set = set()
    for j in s: 
        new_set.add(i|j)
        ans.add(i|j)
    ans.add(i)
    new_set.add(i)
    s = new_set
print(len(ans))
