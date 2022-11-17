N=int(input())
lst=[]

if N%3==0:
    lst.append(int(N/3))
if N%5==0:
    lst.append(int(N/5))

for i in range(1,int(N/3)+1):
    for j in range(1,int(N/5)+1):
        if 3*i+5*j==N:
            lst.append(i+j)
if len(lst)==0:
    print(-1)
else:
    print(min(lst))
