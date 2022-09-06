t = int(input())
while t > 0 :
    n,d = map(int,input().split())
    s = list(map(int,input().split()))
    for i in range(d,n) :
        print(s[i],end = ' ')
    for i in range(0,d) :
        print(s[i],end = ' ')
    print()
    t-=1