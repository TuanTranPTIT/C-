t = 10
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while t>0 :
    h = input()
    if h == '0' :
        break
    else :
        m,s = h.split()
        k = int(m)
        l = len(s)
        x = ''
        for i in range(0, l) :
            for j in range(0, 28) :
                if s[i] == P[j] :
                    x += P[(j+k)%28]
                    break
        print(x[::-1])