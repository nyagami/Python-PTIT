for t in range(int(input())):
    s=input()
    for i in range(0,len(s),2):
        print(s[i]*int(s[i+1]),end='')
    print('')
