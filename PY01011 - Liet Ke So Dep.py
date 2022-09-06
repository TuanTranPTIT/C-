t = int(input())
while t > 0 :
    n = int(input())
    for i in range(22,n,2) :
        s = str(i)
        l = len(s)
        x = int(l/2)
        key = 0
        if(2*x == l) :
            for j in range(0,l) :
                if(s[j] != s[l-1-j] or int(s[j]) % 2 != 0) :
                    key = 1
                    break
            if key == 0 :
                print(i,end=" ")
    print()
    t-=1
