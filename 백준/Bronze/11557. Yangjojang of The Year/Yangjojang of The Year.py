T=int(input())
l1, l2 = [], []
for _ in range(T):
    N=int(input())
    for i in range(N):
        a=tuple(input().split())
        l1.append(a)
        l2.append(int(a[1]))
    mx=max(l2)
    print(l1[l2.index(mx)][0])