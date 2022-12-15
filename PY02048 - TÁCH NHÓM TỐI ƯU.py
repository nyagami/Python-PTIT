n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
gr, i = 0, 0
def up_bow(l, r, x):
    if l>=r: return l
    mid = (l+r)//2
    if a[mid]<=x: return up_bow(mid+1, r, x)
    return up_bow(l, mid, x)
while i<n:
    while True:
        if i>=n : break
        next = up_bow(i+1, n, a[i]+k)
        if next == i+1: break
        else: i = next-1
    i+=1
    gr+=1
print(gr)
