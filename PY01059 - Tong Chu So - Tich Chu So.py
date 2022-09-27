t = int(input())
while(t > 0):
    t -= 1
    n = input()
    l = len(n)
    cnt = 0
    s = 1
    ktra = 0
    for i in range(0,l):
        if(i % 2 == 0):
            cnt += int(n[i])
        else:
            if(n[i] != '0'):
                s *= int(n[i])
                ktra = 1
    if(ktra == 0):
        s = 0
    print(cnt,s)
