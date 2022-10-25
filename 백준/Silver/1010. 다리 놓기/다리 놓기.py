#1010
arr = [[1]*31 for _ in range(31)]

for i in range(31):
    arr[1][i] = i
for i in range(2,31):
    for j in range(i+1,31):
        arr[i][j] = arr[i][j-1]+arr[i-1][j-1]
T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    print(arr[n][m])