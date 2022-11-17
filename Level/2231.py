N=int(input())

for i in range(N):
    s=0
    for j in str(i):
        s+=int(j)
    if s+i==N:
        print(i)
        break
    if i==N:
        print(0)
