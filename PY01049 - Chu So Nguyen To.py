t = int(input())
import math
def prime1(n):
    if(n < 2):
        return 0
    else:
        for i in range(2 , int(math.sqrt(n)) + 1) :
            if( n % i == 0) :
                return 0
        return 1
def prime2(n):
    ng_to = 0
    un_ng_to = 0
    for i in n :
        if( i == '2' or i == '3' or i == '5' or i == '7'):
            ng_to += 1
        else:
            un_ng_to += 1
    if(ng_to > un_ng_to):
        return 1
    else:
        return 0
while( t > 0):
    t -= 1
    n = input()
    l = len(n)
    if(prime1(l) == 1 and prime2(n) == 1):
        print("YES")
    else:
        print("NO")