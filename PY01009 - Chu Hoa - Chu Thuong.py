s = input()
up = 0
low = 0
for i in s :
    if i.isupper() == True :
        up += 1
    if i.islower() == True :
        low += 1
if up > low :
    print(s.upper())
else :
    print(s.lower())