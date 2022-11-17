#1110

n=input()
num=n
count=0


if int(num)<10:
    n='0'+str(num)

while True:
    if len(num)==1:
        num='0'+str(num) 
        sum=int(num[0])+int(num[1]) 
        num=num[-1]+str(sum)[-1]
        count+=1
        
    else:
        sum=int(num[0])+int(num[1])
        num=num[-1]+str(sum)[-1]
        count+=1
    if n == num:
        print(count)
        break
