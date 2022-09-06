t = int(input())
import math
def usc(a, b) :
    if b == 0 :
        return a
    return usc(b, a%b)
while t>0 :
    cnt = 0
    key = 0
    n = int(input())
    for i in range(1, n) :
        if usc(i,n) == 1:
            cnt+=1
    sqr = int(math.sqrt(cnt)) + 1
    for j in range(2,sqr) :
        if cnt % j == 0 :
            key = 1
            break
    if key == 1 or n<3:
        print('NO')
    else :
        print('YES')
    t-=1