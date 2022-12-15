from itertools import permutations
for i in range(int(input())):
    a = list(reversed(list(permutations([str(x) for x in range(1, int(input())+1)]))))
    print(len(a))
    for i in a: print(''.join(i), end=' ')
    print()
