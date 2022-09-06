s = input()
l = len(s)
j = 0
for i in range(0, l) :
    if s[i] == ' ' :
        print(s[j:i],end='\n')
        j = i+1
print(s[j:None])