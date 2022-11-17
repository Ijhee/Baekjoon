e_list=[]
for _ in range(10):
    e_list.append(int(input())%42)
e_list=set(e_list)
print(len(list(e_list)))
