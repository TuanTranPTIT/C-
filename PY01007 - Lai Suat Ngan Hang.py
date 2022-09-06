t = int(input())
while t > 0 :
    n,x,m = map(float,input().split())
    year = 0
    x = x/100
    while n < m :
        n = n + n*x
        year += 1
    print(year)
    t-=1