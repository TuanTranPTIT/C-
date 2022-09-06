t = int(input())
def gt(n) :
    x = 1
    for i in range(1,n+1) :
        x *= i
    return x
while t > 0 :
    n = input()
    cnt = 0
    for i in n :
        cnt += gt(int(i))
    if cnt == int(n) :
        print('Yes')
    else :
        print('No')
    t-=1