n, s, r = map(int, input().split())

demaged = list(map(int,input().split()))
extra = list(map(int,input().split()))

# 카약 정보를 가지는 리스트 생성 후 1으로 초기화
list1 = [1] * n

# 손상된 카약을 가진 팀 = 0 
for i in demaged:
    list1[i-1] -= 1

# 여분의 카약을 가진 팀 = 2
for j in extra:
    list1[j-1] += 1

for k in range(len(list1)):
    # 손상된 카약을 가진 팀이라면
    if list1[k] == 0:
        # 첫번째 원소일때
        if k == 0:
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
        # 마지막 원소일때
        elif k == len(list1)-1:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
        # 중간 원소일때
        else:
            if list1[k-1] == 2:
                list1[k-1] = 1
                list1[k] = 1
                continue              
            if list1[k+1] == 2:
                list1[k+1] = 1
                list1[k] = 1
                continue
    else:
        continue
print(list1.count(0))