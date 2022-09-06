t = int(input())
while t > 0 :
    s = input()
    s += "x"
    l = len(s)
    x = 0
    res = 10**19
    for i in range(1,l):
        if(s[i-1].isdigit()):
            x = x*10 + int(s[i-1])
            if(s[i].isalpha()):
                res = min(res,x)
                x = 0
    print(res)
    t-=1