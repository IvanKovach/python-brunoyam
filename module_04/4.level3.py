# Граф из обучающего видео brunoyam
graph_1 = {'0': set(['1', '2']),
           '1': set(['0', '3', '4']),
           '2': set(['0']),
           '3': set(['1']),
           '4': set(['2', '3'])}

graph_2 = {0: [1, 2],
           1: [0, 3, 4],
           2: [0, 5],
           3: [1],
           4: [1],
           5: [2]}


def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)
    while queue:
        first = queue.pop(0)
        for neighbour in graph[first]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited


print(bfs(graph_1, '3'))
print(bfs(graph_2, 3))
