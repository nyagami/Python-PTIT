def move(start, mid, end, sum):
    if sum==0: return
    move(start, end, mid, sum-1)
    print(f'{start} -> {end}')
    move(mid, start, end, sum-1)
move('A', 'B', 'C', int(input()))
