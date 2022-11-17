while True:
    try:
        num=input().split(' ')
        a,b=int(num[0]),int(num[1])
        print(a+b)
    except:
        print('error')
        break
