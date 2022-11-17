lst=[]
for i in range(100): #원래 10,000,000으로 해야하나 간단하게 100으로 설정
    if i%2==0:
        for j in range(i):
            lst.append(str(j+1)+'/'+str(i-j))
    else:
        for j in range(i):
            lst.append(str(i-j)+'/'+str(j+1))
N=int(input())
print(lst[N-1])
