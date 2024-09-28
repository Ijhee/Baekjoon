n, m, start_node = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited_dfs_dict = dict()
visited_bfs_dict = dict()
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    visited_dfs_dict[a] = False
    visited_dfs_dict[b] = False
    visited_bfs_dict[a] = False
    visited_bfs_dict[b] = False
    
def dfs(graph, start_node, visited_dict):
    visited_dict[start_node] = True
    print(start_node, end=' ')
    for node in sorted(graph[start_node]):
        if not visited_dict[node]:
            dfs(graph,node,visited_dict)
            
def bfs(graph, start_node, visited_dict):
    
    visited_dict[start_node] = True
    unseen_list = [start_node]
    
    while unseen_list:
        search_node = unseen_list.pop(0)
        print(search_node, end=' ')
        for node in sorted(graph[search_node]):
            if not visited_dict[node]:
                visited_dict[node] = True
                unseen_list.append(node)
                
dfs(graph, start_node, visited_dfs_dict)
print()
bfs(graph, start_node, visited_bfs_dict)