t = int(input())
while(t > 0):
    t -= 1
    s = input()
    n = input()
    cnt = 0
    d = s.find(n)
    while(d != -1):
        cnt += 1
        d = s.find(n , d + len(n))
    print(cnt)