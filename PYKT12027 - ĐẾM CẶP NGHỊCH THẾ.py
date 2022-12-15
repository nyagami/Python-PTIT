from sys import stdin
def merge(a, l, mid, r):
    cnt = 0
    pre_ind, pre_cnt = mid + 1, 0
    for i in range(l, mid+1): 
        L, R = pre_ind, r+1
        if L==R or a[i] <= a[pre_ind]:
            cnt += pre_cnt
            continue
        while L<R:
            MID = (L+R)>>1
            if a[MID] < a[i]: L = MID + 1
            else: R = MID
        pre_cnt += L - pre_ind
        cnt += pre_cnt
        pre_ind = L
    a[l:r+1] = sorted(a[l:r+1])
    return cnt
def merge_sort(a, l, r):
    if l >= r: return 0
    mid = (l+r)>>1
    return merge_sort(a, l, mid) + merge_sort(a, mid+1, r) + merge(a, l, mid, r)
n, a = int(stdin.readline()), list(map(int, stdin.readline().split()))
print(merge_sort(a, 0, n-1))
