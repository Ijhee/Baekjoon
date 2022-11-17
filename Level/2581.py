start = int(input())
last = int(input())

lst = []
for num in range(start, last+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            lst.append(num)  # error가 없으면 소수리스트에 추가
            
if len(lst) > 0 :
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
