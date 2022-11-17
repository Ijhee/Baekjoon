N,K=map(int,input().split())
lst=[]
for _ in range(N):
    lst.append(int(input()))
lst=[x for x in lst if x <=K]
lst.sort(reverse=True)

cnt=0
while K>0:
    for i in lst:
        cnt+=(K//i)
        K=K-i*(K//i)
print(cnt)
