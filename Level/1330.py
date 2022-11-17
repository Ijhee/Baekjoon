number=input('숫자를 한 칸 띄어서 입력:')
num_list=number.split(' ')
num1=int(num_list[0])
num2=int(num_list[1])

if num1>num2:
    print('>')
elif num1<num2:
    print('<')
else:
    print('=')
