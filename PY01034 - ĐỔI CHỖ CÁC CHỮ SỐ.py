def mind(s, i):
    ans = i
    for j in range(i+1, len(s)):
        if s[j] < s[i]:
            if ans == i: ans = j
            elif s[ans] < s[j]: ans = j
    if s[ans] < s[i]: return ans
    return -1
for t in range(int(input())):
    s = input()
    n = len(s)
    ans = ''
    for i in range(n-1, -1, -1):
        ind = mind(s, i)
        if ind > -1:
            ans = s[:i] + s[ind] + s[i+1:ind] + s[i] + s[ind+1:]
            break
    if ans!='' and ans!=s and ans[0]!='0': print(ans)
    else: print('-1')
