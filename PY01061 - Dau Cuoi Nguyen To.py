t = int(input())
import math
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n %  i == 0):
            return 0
    return 1
while(t > 0):
    t -= 1
    n = input()
    l = len(n)
    x = int(n[0 : 3])
    y = int(n[l-3 : l])
    if(prime(x) == 1 and prime(y) == 1):
        print("YES")
    else:
        print("NO")