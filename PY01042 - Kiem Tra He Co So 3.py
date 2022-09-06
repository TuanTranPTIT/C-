t = int(input())
while t > 0 :
    n = input()
    key = 0
    l = int(len(n))
    for i in range(l):
        if(n[i] != '0' and n[i] != '1' and n[i] != '2'):
            key = 1
            break
    if key == 1 :
        print("NO")
    else :
        print("YES")
    t-=1