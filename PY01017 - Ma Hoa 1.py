t = int(input())
while t>0 :
    s = input()
    l = len(s)
    cnt = 1
    if l == 1 :
        print('1',s,sep="")
    for i in range(1, l) :
        if s[i] == s[i-1] :
            cnt += 1
        if s[i] != s[i-1] :
            print(cnt,s[i-1],sep="",end="")
            cnt = 1
        if i == l-1 :
            print(cnt,s[i],sep="")
    t-=1