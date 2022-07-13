N,K = map(int, input().split())
lst=[]
for _ in range(N):
    lst.append(int(input()))
lst=sorted(lst,reverse=True)
cnt=0
for x in lst:
    if K>=x:
        cnt+=K//x
        K=K%x
print(cnt)