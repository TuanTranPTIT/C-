from imaplib import Int2AP


t = int(input())
while t>0 :
    s = input()
    l = len(s)/2
    i = 0
    while i < l :
        i1 = i*2 + 1
        i2 = i*2
        x1 = int(s[i1])
        x2 = s[i2]
        for j in range(0, x1) :
            print(x2,end='')
        i+=1
    print(end='\n')
    t-=1