N=int(input())
for _ in range(N):
    e_list=[]
    scores=list(map(int,input().split()))
    avg=sum(scores)/len(scores)
    for x in scores:
        if x>avg:
            e_list.append(x)
    r=len(e_list)/len(scores)*100
    print(f'{r:.3f}%')
