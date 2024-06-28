from collections import deque

head, cnt, node = list(map(int, input().split()))

graph = []
for _ in range(head+1):
    graph.append([])

for _ in range(cnt):
    idx, val = list(map(int, input().split()))
    if graph[idx].count(val) == 0:
        graph[idx].append(val)
    if graph[val].count(idx) == 0:
        graph[val].append(idx)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

dfs_visited = [False] * (head + 1)
bfs_visited = [False] * (head + 1)

dfs_result = []

def dfs(graph, node, visited):
    visited[node] = True
    dfs_result.append(node)
    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            dfs(graph, n, visited)
    
def bfs(graph, node, visited):
    result = []
    visited[node] = True
    bfs_que = deque([node])
    while bfs_que:
        head = bfs_que.popleft()
        result.append(head)
        for n in graph[head]:
            if not visited[n]:
                visited[n] = True
                bfs_que.append(n)
    return result

dfs(graph, node, dfs_visited)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs(graph, node, bfs_visited))))