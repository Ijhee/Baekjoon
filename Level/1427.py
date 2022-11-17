n=int(input())
lst=[]
for i in str(n):
    lst.append(i)
lst.sort(reverse=True)
print(int(''.join(lst)))
