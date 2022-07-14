import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement
N,M = map(int,(input().split()))
lst=[]
for i in range(1,N+1):
    lst.append(i)
data = list(combinations_with_replacement(lst, M) )
for i in data:
    print(' '.join(map(str,list(i))))
  