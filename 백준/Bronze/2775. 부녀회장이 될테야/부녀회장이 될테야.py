T = int(input())
for i in range(T):
    s, r = int(input()), int(input())
    base = [i for i in range(1,r+1)]
    for i in range(s):
        for i in range(1,r):
            base[i] += base[i-1]
    print(base[-1])