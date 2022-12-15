def check(s):
    hit = 0
    for i in s:
        if i!='6' and i!='8': return 'NO'
        if i=='8': hit+=1
        else: hit=0
        if hit==3: return 'NO'
    return 'YES'
print(check(input()))
