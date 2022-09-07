t = int(input())
while(t > 0):
    t -= 1
    s = input()
    s = int(s)
    cnt = 0
    while(s % 7 != 0 and cnt < 1001):
        n = str(s)
        s = int(n) + int(n[::-1])
        cnt += 1
    if(s % 7 == 0):
        print(int(s))
    else:
        print("-1")
