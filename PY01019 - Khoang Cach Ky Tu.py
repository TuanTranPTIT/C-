t = int(input())
while t > 0 :
    s = input()
    l = len(s)
    key = 0
    for i in range(1,l):
        s1 = ord(s[i]) - ord(s[i-1])
        s2 = ord(s[l-i]) - ord(s[l-i-1])
        if s1 != s2 and s1 != (-s2) :
            key = 1
    if key == 1 :
        print("NO")
    else :
        print("YES")
    t-=1