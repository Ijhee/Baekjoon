f1 = 0; f2 = 1
lst = []
N = int(input())
for i in range(N+1):
    if i == 0:
        lst.append(f1)
    elif i == 1:
        lst.append(f2)
    else:
        lst.append(lst[i-1] + lst[i-2])
print(lst[-1])