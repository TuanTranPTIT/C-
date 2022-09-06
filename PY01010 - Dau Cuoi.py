t = int(input())
while t>0 :
    s = input()
    s1 = int(s[None:2])
    s2 = int(s)%100
    if s1 == s2 :
        print('YES')
    else :
        print('NO')
    t-=1