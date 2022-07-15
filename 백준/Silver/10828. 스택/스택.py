import sys
input=sys.stdin.readline
N=int(input())
Stack=[]
        
for _ in range(N):
    fuc=input().split()
    if len(fuc)==2:
        Stack.append(int(fuc[1]))
    else:
        if fuc[0]=='pop':
            if len(Stack)>=1:
                print(Stack[-1])
                Stack.pop(-1)
            elif len(Stack)==0:
                print(-1)
        elif fuc[0]=='size':
            print(len(Stack))
        elif fuc[0]=='empty':
            if len(Stack)==0:
                print(1)
            else:
                print(0)
        elif fuc[0]=='top':
            if len(Stack)>=1:
                print(Stack[-1])
            elif len(Stack)==0:
                print(-1)