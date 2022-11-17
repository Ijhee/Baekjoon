num=int(input())
cnt=2
while num!=1:
  if num%1==0:
    num = num/cnt
    print(cnt)
   else:
    cnt+=1
