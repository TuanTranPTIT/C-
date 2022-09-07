t = int(input())
import math
def prime(n):
    cnt = 0
    for i in n :
        cnt += int(i)
    if(cnt < 2):
        return 0
    else:
        for i in range(2 , int(math.sqrt(cnt)) + 1) :
            if( cnt % i == 0) :
                return 0
        return 1
while( t > 0):
    t -= 1
    n = input()
    if(prime(n) == 1) :
        print("YES")
    else:
        print("NO")