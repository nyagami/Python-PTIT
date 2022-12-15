import re


for t in range(int(input())):
    a = sorted([int(x) for x in re.split("[a-z]+", input()) if x != ''])
    if(len(a)>0): print(a[-1])
