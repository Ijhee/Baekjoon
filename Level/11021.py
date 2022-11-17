case=int(input())
for x in range(1,case+1):
    num=input().split(' ')
    a,b=num[0],num[1]
    print('Case #'+str(x)+':',str(int(a)+int(b)))
