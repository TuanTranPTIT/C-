l,r = map(int,input().split())
import math
for i in range(l , r - 1) :
    for j in range(i + 1 , r ):
        for k in range(j + 1 , r + 1):
            if(math.gcd(i,j) == 1 and math.gcd(j,k) == 1 and math.gcd(k,i) == 1):
                print("(" , i , sep = "", end = "")
                print("," , j , end = "")
                print("," , k , end = "")
                print(")")