c=input()
if c[0]==' ':
    print(len(c[1:].split(' ')))
elif c[-1]==' ':
    print(len(c[:-1].split(' ')))
else:
    print(len(c.split(' ')))
