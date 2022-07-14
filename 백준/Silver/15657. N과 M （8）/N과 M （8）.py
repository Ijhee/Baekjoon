from itertools import combinations_with_replacement
N,M = map(int,(input().split()))
lst = sorted(list(map(int,(input().split()))))
data = list(combinations_with_replacement(lst, M))
for i in data:
    print(*i)