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
def prime_word(n):
    l = len(n)
    for i in range(2 , l):
        x = int(n[i])
        if(prime(i) == 1 and prime(x) == 0):
            return 0
        if(prime(i) == 0 and prime(x) == 1):
            return 0
    return 1
        
while(t > 0):
    t -= 1
    n = input()
    if(prime_word(n) == 1):
        print("YES")
    else:
        print("NO")
    