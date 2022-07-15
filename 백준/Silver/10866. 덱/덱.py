import sys
input = sys.stdin.readline
N=int(input())
Deque=[]
        
for _ in range(N):
    fuc=input().split()
    if len(fuc)==2:
        if fuc[0]=='push_front':
            Deque.insert(0,int(fuc[1]))
        elif fuc[0]=='push_back':
            Deque.append(fuc[1])
    else:
        if fuc[0]=='pop_front':
            if len(Deque)>=1:
                print(Deque[0])
                Deque.pop(0)
            elif len(Deque)==0:
                print(-1)
        if fuc[0]=='pop_back':
            if len(Deque)>=1:
                print(Deque[-1])
                Deque.pop(-1)
            elif len(Deque)==0:
                print(-1)
                
        elif fuc[0]=='size':
            print(len(Deque))
            
        elif fuc[0]=='empty':
            if len(Deque)==0:
                print(1)
            else:
                print(0)
                
        elif fuc[0]=='front':
            if len(Deque)>=1:
                print(Deque[0])
            elif len(Deque)==0:
                print(-1)
                
        elif fuc[0]=='back':
            if len(Deque)>=1:
                print(Deque[-1])
            elif len(Deque)==0:
                print(-1)