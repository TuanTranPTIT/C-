n,k = map(int,input().split())
import math
d = 0
for i in range(10**(k-1), 10**k):
    if(math.gcd(i,n) == 1):
        print(i,end=" ")
        d +=1
    if(d == 10) :
        print()
        d = 0