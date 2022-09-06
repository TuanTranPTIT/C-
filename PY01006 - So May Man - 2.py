t = int(input())
while t > 0 :
    key = 0
    n = input()
    for i in n :
        if i != '4' and i != '7' :
            key = 1
            break
    if key == 0 :
        print('YES')
    else :
        print('NO')
    t-=1