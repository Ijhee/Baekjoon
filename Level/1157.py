S=input()
S=S.upper()
s=set(S)
l=[]
for x in s:
    l.append(S.count(x))
if l.count(max(l))>1:
    print('?')
else:
    for x in S:
        if S.count(x)==max(l):
            print(x)
            break
