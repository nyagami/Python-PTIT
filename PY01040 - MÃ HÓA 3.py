def turn(s):
    sum = 0 
    for i in s: sum += ord(i) - ord('A')
    r = ''
    for i in s: r += chr((ord(i) - ord('A') + sum) % 26 + ord('A'))
    return r
for t in range(int(input())):
    s = input()
    a, b = turn(s[:len(s)//2]), turn(s[len(s)//2:])
    r = ''
    for i in range(len(a)):
        r += chr((ord(a[i]) + ord(b[i]) - 2*ord('A')) % 26 + ord('A'))
    print(r)
