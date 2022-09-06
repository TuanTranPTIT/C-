t = int(input())
while t>0 :
    n = input()
    if int(n) < 10 :
        print(n)
    else :
        i = len(n)-2
        x = 10 ** i
        x1 = 10 * x
        y=int(n) % x1
        if int(y) > 4.44444444*x :
            print((int(n[0])+1)*x1)
        else :
            print(int(n[0])*x1)
    t-=1