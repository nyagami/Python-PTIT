from sys import stdin
# input = open("d:/code/in.txt").readline
input = stdin.readline
a, n = [], int(input())
for i in range(n): a.append(int(input()))

def low(arr, L, x):
    R = len(arr)-1
    while L<R:
        mid = (L+R)>>1
        if arr[mid]<x: L = mid+1
        else: R = mid
    return L

z = sorted(set(a))
m = [[] for i in z]
first = [0]*len(z)

for i in range(n):
    a[i] = low(z, 0, a[i])
    m[a[i]].append(i)

def get(arr, start, end, step, root):
    st = [] 
    for i in range(start, end, step):
        while len(st)>0 and a[st[-1]] <= a[i]: st.pop()
        arr[i] = root if len(st)==0 else st[-1]
        st.append(i)

l, r = [0]*n, [0]*n
get(l, 0, n, 1, -1)
get(r, n-1, -1, -1, n)

def count(arr, start, end):
    if start >= len(arr) or end < arr[start]: return 0
    pos = low(arr, start, end)
    if arr[pos] > end: pos-=1
    return pos - start + 1
s = 0
for i in range(n):
    if l[i]!=-1: s+=1
    if r[i]!=n: s+=1
    x = count(m[a[i]], first[a[i]], r[i] - 1)
    s += (x-1)*x//2
    first[a[i]]+=x

print(s)
