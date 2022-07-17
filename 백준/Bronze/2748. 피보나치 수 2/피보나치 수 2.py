N=int(input())
n1=0
n2=1
n3=1
x=0
for i in range(N-2):
    x=n3
    n3=n2+n3
    n2=x
print(n3)