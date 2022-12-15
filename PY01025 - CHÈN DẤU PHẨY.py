s=input()
ans=s[-3:]
for i in range(len(s)-3,0,-3):
    ans=(s[i-3:i] if i-3>=0 else s[:i]) + ',' + ans
print(ans)
