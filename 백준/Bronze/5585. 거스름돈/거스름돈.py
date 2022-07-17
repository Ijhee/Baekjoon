M=[500,100,50,10,5,1]
B=1000-int(input())

cnt=0
for i in M:
    if B//i!=0:
        cnt+=B//i
        B=B%i
    else:
        pass
print(cnt)