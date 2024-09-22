N = int(input())
game_map = []
for _ in range(N):
    game_map.append(list(map(int,input().split())))

need_visited = list(); visted = list()
start_node = game_map[0][0]
need_visited.append((start_node,0,0))

answer_flag = True
while need_visited:

    node = need_visited.pop()
    if node[0] == 1:
        try:
            need_visited.append((game_map[node[1]+1][node[2]],node[1]+1,node[2]))
        except:
            pass
        try:
            need_visited.append((game_map[node[1]][node[2]+1],node[1],node[2]+1))
        except:
            pass
    elif node[0] == 2:
        try:
            need_visited.append((game_map[node[1]+2][node[2]],node[1]+2,node[2]))
        except:
            pass
        try:
            need_visited.append((game_map[node[1]][node[2]+2],node[1],node[2]+2))

        except:
            pass
    else:
        pass

    if node[0] == -1:
        answer_flag = False
        print('HaruHaru')
        break
    
if answer_flag:
    print('Hing')