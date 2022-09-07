t = int(input())
import math
while( t > 0):
    t -= 1
    n = input()
    cnt = 1
    for i in n :
        if(i != '0'):
            cnt *= int(i)
    print(cnt)