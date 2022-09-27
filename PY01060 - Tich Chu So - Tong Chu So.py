t = int(input())
while(t > 0):
    t -= 1
    n = input()
    l = len(n)
    cnt = 0
    s = 1
    for i in range(0,l):
        if(i % 2 != 0):
            cnt += int(n[i])
        else:
            if(n[i] != '0'):
                s *= int(n[i])
    print(s,cnt)