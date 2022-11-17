l,a,b,c,d = map(int,input().split())

e = a // c
f = b // d

if e > f:
    if a % c == 0:
        print(l - e)
    else:
        print(l - 1 - e)
else:
    if b % d == 0:
        print(l - f)
    else:
        print(l - 1 - f)
