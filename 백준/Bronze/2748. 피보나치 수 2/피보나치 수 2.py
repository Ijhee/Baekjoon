N = int(input())
f = 0
s = 1
lst = []
for i in range(N+1):
    if i == 0:
        lst.append(f)
    elif i == 1:
        lst.append(s)
    else:
        lst.append(lst[i-2]+lst[i-1])
print(lst[-1])