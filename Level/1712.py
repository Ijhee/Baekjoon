A=int(input())
B=int(input())
C=int(input())
if (C - B) <= 0:
    print("-1")
else:
    N = A / (C - B)
    N = N + 1
    print(int(N))
