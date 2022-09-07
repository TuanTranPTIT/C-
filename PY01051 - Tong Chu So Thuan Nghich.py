t = int(input())
while(t > 0):
    t -= 1
    n = input()
    cnt = 0
    for i in n:
        cnt += int(i)
    cnt = str(cnt)
    if(int(cnt) > 10 and cnt == cnt[::-1]):
        print("YES")
    else:
        print("NO")