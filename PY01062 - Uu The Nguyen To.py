import math
t = int(input())
def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n %  i == 0):
            return 0
    return 1
while(t > 0):
    t -= 1
    n = input()
    cnt_Prime = 0
    no_Cnt_Prime = 0
    for i in n :
        if(prime(int(i)) == 1):
            cnt_Prime += 1
        else:
            no_Cnt_Prime += 1
    if(cnt_Prime > no_Cnt_Prime and prime(len(n)) == 1):
        print("YES")
    else:
        print("NO")