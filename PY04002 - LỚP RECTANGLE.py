import sys
class Rectangle:
    def __init__(self, a, b, c) -> None:
        self.perimeter = (a+b)*2
        self.area = a*b
        self.color = c[:1].upper() + c[1:].lower()

arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print('{} {} {}'.format(r.perimeter, r.area, r.color)) 
else: print('INVALID')
sys.exit()
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
        t -= 1

