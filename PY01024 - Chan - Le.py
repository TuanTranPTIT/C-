t = int(input())
while t>0 :
    n = input()
    cnt = 0
    l = len(n) - 1
    key = 0
    for i in n :
        cnt += int(i)
    for j in range(0, l) :
        x = int(n[j]) - int(n[j+1])
        if x != 2 and x != -2 :
            key = 1
    if key == 0 and cnt%10 == 0 :
        print('YES')
    else :
        print('NO')
    t-=1