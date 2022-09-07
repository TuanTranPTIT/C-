t = int(input())
import math
def prime(n):
    if(n < 2):
        return 0
    else:
        for i in range(2 , int(math.sqrt(n)) + 1) :
            if( n % i == 0) :
                return 0
        return 1


while( t > 0):
    t -= 1
    s = input()
    l = len(s)
    n = int(s[l-4:l])
    if(prime(n) == 1) :
        print("YES")
    else:
        print("NO")