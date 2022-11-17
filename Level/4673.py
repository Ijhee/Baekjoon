num_list=list(range(1,10001))
r_list=[]
for i in num_list:
    for j in str(i):
        i+=int(j)
    if i<=10000:
        r_list.append(i)
for x in set(r_list):
    num_list.remove(x)
for x in num_list:
    print(x)
