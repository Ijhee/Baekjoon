import sys
input=sys.stdin.readline
N=int(input())
lst=[]
for i in range(N):
    lst.append(input().split())
lst = sorted(lst, key = lambda x : int(x[0]))
for i1,i2 in lst:
    print(i1,i2)