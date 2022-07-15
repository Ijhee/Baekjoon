import sys
input=sys.stdin.readline
N=int(input())
que=[]
        
for _ in range(N):
    fuc=input().split()
    if len(fuc)==2:
        que.append(int(fuc[1]))
    else:
        if fuc[0]=='pop':
            if len(que)>=1:
                print(que[0])
                que.pop(0)
            elif len(que)==0:
                print(-1)
        elif fuc[0]=='size':
            print(len(que))
        elif fuc[0]=='empty':
            if len(que)==0:
                print(1)
            else:
                print(0)
        elif fuc[0]=='front':
            if len(que)>=1:
                print(que[0])
            elif len(que)==0:
                print(-1)
        elif fuc[0]=='back':
            if len(que)>=1:
                print(que[-1])
            elif len(que)==0:
                print(-1)