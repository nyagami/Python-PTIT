from itertools import combinations

n,k=input().split()
comb = combinations(sorted(set(input().split()),key=int),int(k))
print('\n'.join([' '.join(x) for x in comb]))
    

        
    
