N=int(input())
e_list=[]
new_list=[]
for _ in range(N):
    e_list.append(int(input()))
for i in range(N):
    new_list.append((e_list[i]/max(e_list))*100)
print(sum(new_list)/N)
