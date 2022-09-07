t = int(input())
import math
def prime(n):
    if(n<2):
        return 0
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if(n % i == 0):
                return 0
        return 1
while(t > 0):
    t -= 1
    n = input()
    l = len(n)
    key = 1
    cnt = 0
    for i in range(0 , l):
        if((i % 2 == 0 and int(n[i]) % 2 != 0) or (i % 2 == 1 and int(n[i]) % 2 !=1)):
            key = 0
            break
        cnt += int(n[i])
    if(prime(cnt) == 1 and key == 1):
        print("YES")
    else:
        print("NO")