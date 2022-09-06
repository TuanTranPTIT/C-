from multiprocessing.sharedctypes import Value
from re import X


n = int(input())
dic = {}
while n > 0 :
    s = input()
    dic[s] = 1
    n-=1
print(len(dic))

