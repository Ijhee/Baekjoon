N, M = map(int,(input().split()))
lst1 = []
for _ in range(N):
    lst1.append(list(map(int,(input().split()))))

M, K = map(int,(input().split()))
lst2 = []
for _ in range(M):
    lst2.append(list(map(int,(input().split()))))

S = [[0] * K for _ in range(N)]

for n in range(N):
    for m in range(M):
        for k in range(K):
            S[n][k] += lst1[n][m] * lst2[m][k]

for n in range(N):
    for k in range(K):
        print(S[n][k], end = " ")
    print('')