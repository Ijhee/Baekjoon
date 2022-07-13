N=int(input())
lst=[]
for i in range(N):
    lst.append(list(map(int,input().split())))
for i1,i2 in sorted(lst, key = lambda x : (x[0],x[1])):
    print(i1,i2)