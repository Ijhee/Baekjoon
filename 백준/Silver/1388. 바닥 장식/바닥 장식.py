row,col = map(int,input().split())

floor = []

for _ in range(int(row)):
    floor.append(input().strip())

cnt = 0
for r in range(row):
    c = 0
    while c <= col-1: 
        current_val = floor[r][c]
        if current_val == '-':
            row_flag = True
            if c>= col-1:
                c += 1
            else:
                # -가 몇개 연속으로 있는지
                while row_flag:
                    if floor[r][c+1] == '-':
                        c += 1
                        # 행 내 마지막 원소까지 다 돌았을 경우
                        if c >= col-1:
                            # while문 나오기
                            row_flag = False
                            # 전체 while문 나오기
                            c += 1
                    else:
                        c += 1 #5
                        row_flag = False
            cnt += 1

        else:
            c+=1
                

for c in range(col):
    r = 0
    while r <= row-1:
        current_val = floor[r][c]
        if current_val == '|':
            col_flag = True
            if r >= row-1:
                r += 1
            else:
                while col_flag:
                    if floor[r+1][c] == '|':
                        r += 1
                        if r >= row-1:
                            col_flag = False
                            r += 1
                    else:
                        r += 1
                        col_flag = False
            cnt += 1
        else:
            r += 1

print(cnt)