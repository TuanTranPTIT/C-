t = int(input())
while t>0 :
    n = input()
    key = 0
    i=0
    while i < len(n) - 1  :
        if int(n[i:i+1]) > int(n[i+1:i+2]) :
            print('NO')
            key = 1
            break
        i+=1
    if key == 0 :
        print('YES')
    t-=1