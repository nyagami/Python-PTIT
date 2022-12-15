f=[0,1]
for i in range(2,93): f.append(f[i-1]+f[i-2])
for t in range(int(input())):
    a,b=input().split()
    for i in range(int(a),int(b)+1): print(f[i],end=' ')
    print('')
