while True:
    lst = list(map(int,input().split()))
    lst=sorted(lst)
    if lst==[0, 0, 0]:
        break
    else:
        if lst[2]**2 == lst[0]**2+lst[1]**2:
            print('right')
        else:
            print('wrong')