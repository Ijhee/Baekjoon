a = 0 ; b = 1 ; c = 1
N = int(input())
for i in range(N):
    c = a
    a = (a+b)%1000000007 ; b = c%1000000007
print(a)