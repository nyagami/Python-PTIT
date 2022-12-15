pre, ans, _ = -1, [], input()
try:
    while True:
        l = len(input().split())
        if l == 6: 
            input()
            if l != pre: ans.append(1)
        else: 
            ans.append(2)
            for i in range(3): input()
        pre = l
except: pass
print(len(ans))
for i in ans: print(i)

