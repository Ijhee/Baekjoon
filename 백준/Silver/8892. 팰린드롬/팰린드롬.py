def Palindrom():
    n = int(input())
    lst = [input() for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                s = lst[i] + lst[j]
                if s == s[::-1]:
                    return s
    return 0

T = int(input())

for _ in range(T):
    ans = Palindrom()
    print(0) if ans == 0 else print(ans)