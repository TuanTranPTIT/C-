n = input()
l = len(n)
x = l%3
if x == 0 :
    x = 3
s = n[None:x]
for i in range(x,l,3) :
    s += ',' + n[i:i+3]
print(s)