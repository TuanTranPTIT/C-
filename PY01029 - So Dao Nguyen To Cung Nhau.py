t = int(input())
def ucl(a,b):
    if b == 0 :
        return a
    return ucl(b,a%b)
while t > 0 :
    a = input()
    b = a[::-1]
    if ucl(int(a),int(b)) == 1 :
        print('YES')
    else :
        print('NO')
    t-=1