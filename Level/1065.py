N=input()
cnt=0
if len(N)<=2:
    print(N)
else:
    for x in range(100,int(N)+1):
        if int(str(x)[2])-int(str(x)[1])==int(str(x)[1])-int(str(x)[0]):
            cnt+=1
    print(cnt+99)
