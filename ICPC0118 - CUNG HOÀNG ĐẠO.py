import os
from datetime import date
def zodiac(Day, Month):
    if ((int(Month)==12 and int(Day) >= 22)or(int(Month)==1 and int(Day)<= 19)):
        return 'Ma Ket'
    elif ((int(Month)==1 and int(Day) >= 20)or(int(Month)==2 and int(Day)<= 18)):
        return 'Bao Binh'
    elif ((int(Month)==2 and int(Day) >= 19)or(int(Month)==3 and int(Day)<= 20)):
        return 'Song Ngu'
    elif ((int(Month)==3 and int(Day) >= 21)or(int(Month)==4 and int(Day)<= 19)):
        return 'Bach Duong'
    elif ((int(Month)==4 and int(Day) >= 20)or(int(Month)==5 and int(Day)<= 20)):
        return 'Kim Nguu'
    elif ((int(Month)==5 and int(Day) >= 21)or(int(Month)==6 and int(Day)<= 20)):
        return 'Song Tu'
    elif ((int(Month)==6 and int(Day) >= 21)or(int(Month)==7 and int(Day)<= 22)):
        return 'Cu Giai'
    elif ((int(Month)==7 and int(Day) >= 23)or(int(Month)==8 and int(Day)<= 22)): 
        return 'Su Tu'
    elif ((int(Month)==8 and int(Day) >= 23)or(int(Month)==9 and int(Day)<= 22)): 
        return 'Xu Nu'
    elif ((int(Month)==9 and int(Day) >= 23)or(int(Month)==10 and int(Day)<= 22)):
        return 'Thien Binh'
    elif ((int(Month)==10 and int(Day) >= 23)or(int(Month)==11 and int(Day)<= 22)): 
        return 'Thien Yet'
    else: return 'Nhan Ma'
for t in range(int(input())):
    d, m = input().split()
    print(zodiac(d,m))
