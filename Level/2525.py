h,m1,m2 = map(int,input().split())

hour=h+((m1+m2)//60)
min=m1+m2-60*((m1+m2)//60)
if hour>=24:
    print(hour-24,min)
else:
    print(hour,min)
