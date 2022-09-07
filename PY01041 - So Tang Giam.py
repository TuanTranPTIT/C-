t = int(input())
while(t > 0):
    t -= 1
    n = input()
    l = len(n)
    key = 0
    key = 1
    for i in range(0 , l - 1):
        if(n[i] >= n[i + 1]):
            k = i
            break
    for i in range(k , l - 1):
        if(n[i] <= n[i + 1]):
            key = 0
            break
    if(l > 2 and key == 1):
        print("YES")
    else:
        print("NO")
