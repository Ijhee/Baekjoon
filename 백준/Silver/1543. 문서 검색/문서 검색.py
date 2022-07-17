S=input()
P=input()
cnt=0

while P in S:
    idx=S.find(P)
    S=S[idx+len(P):]
    cnt+=1
print(cnt)