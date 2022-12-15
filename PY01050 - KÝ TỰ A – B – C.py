n = int(input())
def Try(i, cnt: dict, sum, s: str):
    if i==sum:
        for c in cnt:
            if cnt[c] == 0: return
        if cnt['A'] > cnt['B'] or cnt['B'] > cnt['C']: return
        print(s)
        return
    for c in 'ABC':
        cnt[c]+=1
        Try(i+1, cnt, sum, s+c)
        cnt[c]-=1
for i in range(3,n+1):
    cnt = {'A': 0, 'B':0, 'C':0}
    Try(0, cnt, i, '')
