from math import sqrt, pow, pi
a, b = map(float, input().split())
c = sqrt(a*a+b*b)
r = (a+b-c)/2
x = sqrt(pow(b-r,2) + r*r)
k = (x-r)/(x+r)
p = 2*pi*pow(r,2)/(1-pow(k,2))/a/b
print(f'{p:.4f}')
