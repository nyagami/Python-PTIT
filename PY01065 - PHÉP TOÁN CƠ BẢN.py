def check(a, op , b, ans):
    if op == '+': return a+b == ans
    if op == '-': return a-b == ans
    if op == '*': return a*b == ans
    if a%b==0: return a//b == ans
    return False

def genn(a):
    ans = []
    if a[0] == '?':
        for i in range(1, 10): ans.append(str(i) + a[1:])
    else: ans.append(a)
    r = []
    if a[1] == '?':
        for i in ans:
            for j in range(0, 10): r.append(i[0] + str(j))
    else: r = ans
    return r
def geno(x):
    if x == '?': return "+-&/"
    return [x]  

def solve(s):
    arr = s.split()
    a = genn(arr[0])
    op = geno(arr[1])
    b = genn(arr[2])
    ans = genn(arr[4])
    for i in a:
        for j in op:
            for k in b:
                for m in ans:
                    if(check(int(i), j, int(k), int(m))):
                        print(f'{i} {j} {k} = {m}')
                        return
    print('WRONG PROBLEM!')

for t in range(int(input())): solve(input())
