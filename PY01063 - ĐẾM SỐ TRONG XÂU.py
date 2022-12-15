for t in range(int(input())):
    s=input()
    n=input()
    i=0
    c=0
    while(i<len(s)):
        x=s.find(n,i)
        if x==-1: break
        else:
            c+=1
            i=x+len(n)  
    print(c)
        
    
