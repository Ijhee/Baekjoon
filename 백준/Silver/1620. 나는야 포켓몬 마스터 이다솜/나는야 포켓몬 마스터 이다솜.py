import sys
input=sys.stdin.readline
N, M = map(int, input().split())
S=[]
for i in range(N):
    s=input().rstrip()
    S.append([i+1,s])
dic=dict(S)
bb = {v:k for k,v in dic.items()}
for _ in range(M):
    a=input().rstrip()
    if a.isdigit():
        print(dic[int(a)])
    else:
        print(bb[a])