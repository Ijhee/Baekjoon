N = int(input())
c = 4
lst = [0,1]
for i in range(N):
    if i == 0 : pass
    else:
        c = c+((lst[i-1]+lst[i])*2)
        lst.append(lst[i-1]+lst[i])
print(c)