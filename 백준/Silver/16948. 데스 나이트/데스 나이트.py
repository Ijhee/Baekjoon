N = int(input())
start_row, start_col, end_row, end_col = map(int,input().split())

visited = [[False for i in range(N)] for _ in range(N)] # 방문 여부 기록 행렬
time = [[0 for i in range(N)] for _ in range(N)] # 각 노드에 도달하는 시간 기록

from collections import deque
need_visit = deque([(start_row,start_col)]) # 방문한 노드의 탐색 후보 노드->(행,열) 형태로 저장

answer_flag = True; flag = True
while flag:
    start_point = need_visit.popleft()
    row, col = start_point[0], start_point[1] # pop한 노드의 행,열 받아오기
    
    for cand_row, cand_col in [(row-2,col-1),(row-2,col+1),(row,col-2),(row,col+2),(row+2,col-1),(row+2,col+1)]: # 탐색 후보 노드
        # 정답 위치에 도달했을 경우
        if cand_row == end_row and cand_col == end_col:
            print(time[row][col]+1)
            flag = False
            answer_flag = False
            break
        # 아직 방문하지 않은 노드들 중에서 탐색 -> 같은 위치에 있는 노드는 항상 갈 수 있는 위치가 정해져 있기 때문에 이미 방문하였을 경우, 다음 차례에 방문하면 이미 최소 이동 횟수가 뒤쳐짐
        # 체스판 크기 내에서 이동할 수 있는 노드들만
        if 0<=cand_row<=N-1 and 0<=cand_col<=N-1 and not visited[cand_row][cand_col]:
            # 후보 노드 -> 탐색 후보 노드 deque에 저장
            need_visit.append((cand_row,cand_col))
            time[cand_row][cand_col] = time[row][col]+1
            visited[cand_row][cand_col] = True # 방문 여부 -> True
    # 다 탐색을 하였는데도, answer_flag가 변하지 않았을 경우 break
    if not need_visit:
        flag=False
# 정답 flag가 False -> 이동할 수 없는 경우로 -1
if answer_flag:
    print(-1)
