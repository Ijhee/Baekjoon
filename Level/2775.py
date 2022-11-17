T=int(input())
for _ in range(T):
    floor=int(input())
    room=int(input())
    lst=[x for x in range(1,room+1)]
    for i in range(floor):
        for j in range(1,room):
            lst[j]+=lst[j-1]
    print(lst[-1])
