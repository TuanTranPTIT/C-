t = int(input())
import math
def prime(n):
    cnt = 0
    for i in n :
        cnt += int(i)
    if(cnt % 3 == 0):
        return 1
    else :
        return 0
while( t > 0):
    t -= 1
    n = input()
    if(prime(n) == 1) :
        print("YES")
    else:
        print("NO")