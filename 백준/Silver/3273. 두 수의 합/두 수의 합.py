import sys
input=sys.stdin.readline

N=int(input())
lst=sorted(list(map(int,input().split())))
res=int(input())

cnt=0
for i in lst:
    if res-i in lst:
        if 2*i==res:
            pass
        else:
            lst.remove(res-i)
            cnt+=1
print(cnt)