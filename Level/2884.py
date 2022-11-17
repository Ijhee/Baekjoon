hour=int(input('시 입력:'))
minute=int(input('분 입력:'))

time1=hour*60+minute
time2=time1-45
if hour==0 and minute<45:
    print('23',str(60+minute-45))
else :
    h,m=divmod(time2,60)
    print(h,m)
