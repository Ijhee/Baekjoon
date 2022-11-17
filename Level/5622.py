alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word=input()
time=0
for i in range(len(word)):
    for j in alpha:
        if word[i] in j:
            time+=alpha.index(j)+3
print(time)
