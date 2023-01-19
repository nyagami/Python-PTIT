from itertools import permutations

def check1(a, A, B, C, s):
    return a[C[0]] + a[A[0]] + a[B[0]] + a[C[1]] == s and \
    a[C[0]] + a[A[1]] + a[C[2]] + a[C[4]] == s and \
    a[C[1]] + a[B[1]] + a[C[3]] + a[C[4]] == s and \
    a[A[2]] + a[C[2]] + a[C[3]] + a[B[2]] == s
def check2(a, A, B, C, s):
    return a[A[0]] + a[B[1]] + a[C[1]] + a[C[4]] == s and \
    a[A[2]] + a[C[0]] + a[C[2]] + a[C[4]] == s and \
    a[B[0]] + a[A[1]] + a[C[0]] + a[C[3]] == s and \
    a[B[2]] + a[C[1]] + a[C[2]] + a[C[3]] == s

for t in range(int(input())):
    a = list(map(int, input().split()))
    s = sum(a)
    if s % 3 != 0:
        print(0)
        continue
    s //= 3
    V = []
    for i in range(1, 12):
        for j in range(1, i):
            for k in range(1, j):
                if a[i] + a[j] + a[k] + a[0] == s:
                    V.append((k, j, i))
    
    sz = len(V)
    ans = 0
    A, B, C =[0]*3, [0]*3, [0]*5

    for i in range(sz):
        used = [False]*12
        A[0], A[1], A[2] = V[i]
        used[A[0]], used[A[1]], used[A[2]] = True, True, True
        for j in range(i):
            if (not used[V[j][0]]) and (not used[V[j][1]]) and (not used[V[j][2]]):
                B[0], B[1], B[2] = V[j]
                used2 = [False]*12
                used2[A[0]], used2[A[1]], used2[A[2]] = True, True, True
                used2[B[0]], used2[B[1]], used2[B[2]] = True, True, True
                cnt = 0
                for k in range(1, 12):
                    if not used2[k]:
                        C[cnt] = k
                        cnt += 1
                for pa in permutations(A):
                    for pb in permutations(B):
                        for pc in permutations(C):
                            if check1(a, pa, pb, pc, s):
                                ans += 1
                            if check2(a, pa, pb, pc, s):
                                ans += 1
    print(ans)
                
