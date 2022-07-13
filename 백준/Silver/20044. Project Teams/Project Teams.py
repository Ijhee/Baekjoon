N=int(input())
T=sorted(list(map(int,input().split())))
l=[]
for i in range(N):
    l.append(T[i]+T[2*N-1-i])
print(min(l))