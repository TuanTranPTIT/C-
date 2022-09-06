t = int(input())
while t > 0 :
    n = input()
    key = 0
    l = int(len(n))-2
    for i in range(l):
        if(n[i] != n[i+2]):
            key = 1
            break
    if key == 1 :
        print("NO")
    else :
        print("YES")
    t-=1