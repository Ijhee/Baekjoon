A=int(input())
B=int(input())
C=int(input())

result=str(A*B*C)
for x in range(10):
    print(result.count(str(x)))
