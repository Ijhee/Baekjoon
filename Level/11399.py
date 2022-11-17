N=int(input())
cus=list(map(int,input().split()))
cus.sort()

s=0
for x in cus:
    s+=x*N
    N-=1
print(s)
