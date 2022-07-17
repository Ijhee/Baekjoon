N, M = map(int,input().split())
S, A =[],[]
for _ in range(N):
    s=input()
    S.append(s.split())
for _ in range(M):
    A.append(input())
dic=dict(S)
for x in A:
    if x in dic.keys():
        print(dic[x])