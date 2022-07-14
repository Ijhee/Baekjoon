from itertools import combinations
N,M = map(int,(input().split()))
lst=[]
for i in range(1,N+1):
    lst.append(i)
c=combinations(lst,M)
for x in list(c):
    print(' '.join(map(str,list(x))))