t = int(input())
import math
def ucln(a, b) :
    if b == 0 :
        return a
    return ucln(b, a%b)
while t>0 :
    a,b = map(int,input().split())
    s = str(ucln(a, b))
    sum = 0
    key = 0
    for i in s :
        sum += int(i)
    if sum == 1 :
        print('NO')
    else :
        sqr = int(math.sqrt(sum)) +1
        for j in range(2,sqr) :
            if sum % j == 0 :
                key = 1
                break
        if key == 1 :
            print('NO')
        else :
            print('YES')
    t-=1