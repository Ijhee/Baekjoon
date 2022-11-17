#1137
n=int(input())
lst=[]
for x in range(n):
    lst.append(input())
lst=list(set(lst))
lst.sort()
lst.sort(key=len)
for y in lst:
    print(y)
