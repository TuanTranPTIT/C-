t = int(input())
while(t > 0):
    t -= 1
    n = input()
    l = len(n)
    key = 1
    for i in range(0,l-2,2):
        if(n[i] != n[i+2]):
            key = 0
    if(l % 2 == 1 and n[0] != n[1] and key == 1):
        print("YES")
    else:
        print("NO")