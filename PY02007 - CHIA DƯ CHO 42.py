a={}
while True:
    try:
        s=input()
        if s=='': continue
        for i in s.split(): a[int(i)%42]=1
    except: break
print(len(a))
