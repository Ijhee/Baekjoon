#12018 : Yonsei ToTo
Seung_Sub,Seung_ML = map(int,input().split())
C_list=[]

for i in range(Seung_Sub):
    Sub,ML = map(int,input().split())
    Stud=sorted(list(map(int,input().split())))
    if Sub>=ML:
        Stud.sort(reverse=True)
        C_list.append(Stud[ML-1])
    else:
        C_list.append(1)

C_list.sort()

s=0; cnt=0
for i in range(len(C_list)):
    s+=C_list[i]
    if s<=Seung_ML:
        cnt+=1
    else:
        break
print(cnt)