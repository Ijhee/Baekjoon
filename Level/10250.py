H=int(input())
W=int(input())
N=int(input())
cnt=0
for i in range(1,W+1):
    for j in range(1,H+1):
        cnt+=1
        if cnt==N:
            if i<=9:
                print(str(j)+'0'+str(i))
            else:
                print(str(j)+str(i))
