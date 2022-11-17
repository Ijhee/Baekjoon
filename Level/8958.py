N=int(input())
for _ in range(N):
    ox=input()
    score=0
    count=0
    for i in range(len(ox)):
        if ox[i]=='O':
            count+=1
            score+=count
        elif ox[i]=='X':
            count=0
    print(score)
