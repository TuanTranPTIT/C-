a,k,n = map(int,input().split())
if a >= n :
    print('-1')
else :
    key = 0
    x = (n // k) + 1
    for i in range(1,x) :
        b = i * k - a
        if b > 0 :
            print(b,end=' ')
            key = 1
    if key == 0 :
        print('-1')