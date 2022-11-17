e_list=[]
for _ in range(9):
    e_list.append(int(input()))
m=max(e_list)
print(m)
print(e_list.index(m)+1)
