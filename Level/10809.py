A='abcdefghijklmnopqrstuvwxyz'
B=input()
for x in A:
    if x in B:
        print(list(B).index(x),end=' ')
    else:
        print('-1',end=' ')
