def Try(s):
    if len(s) == 1: return
    a = int(s[:len(s)//2])
    b = int(s[len(s)//2:])
    print(a+b)
    Try(str(a+b))
Try(input())
