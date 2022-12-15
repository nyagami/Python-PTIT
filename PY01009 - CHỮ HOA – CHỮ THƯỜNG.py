s=input()
print(s.lower()) if [x for x in s if x.islower()].__len__()*2 >= s.__len__() else print(s.upper())
