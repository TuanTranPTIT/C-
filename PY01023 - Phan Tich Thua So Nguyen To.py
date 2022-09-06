t = int(input())
import math
while t > 0 :
    n = int(input())
    print('1',end='')
    sqr = int(math.sqrt(n)) +1
    for i in range(2,sqr) :
        cnt = 0
        while n % i == 0 :
            cnt+=1
            n/=i
        if cnt > 0 :
            print(' * ', i, '^', cnt,sep='',end='')
    if n > (sqr-1) :
       print(' * ', int(n) ,'^1',sep='' ) 
    else :
        print()
    t-=1
